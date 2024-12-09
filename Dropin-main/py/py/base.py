from typing import Any, Union, Dict, Collection
import string
import uuid
import json
import functools
import datetime
import decimal

from tornado.web import RequestHandler, HTTPError
from tornado.options import options
from tornado.log import app_log

CHARS = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'


def uuid22():
    h32 = F'{uuid.uuid4().hex}'
    # 32 位长度，转为 11 组，3个一组
    # 0xfff == 64 * 64 - 1\
    s22: list[str] = []
    for i in range(11):
        ifff = int(h32[(i * 3):(i * 3 + 3)], 16)
        s22.append(F'{CHARS[ifff // 64]}{CHARS[ifff % 64]}')
    return ''.join(s22)


def authenticated(method):
    @functools.wraps(method)
    def wrapper(  # type: ignore
        self: RequestHandler, *args, **kwargs
    ):
        if not self.current_user:
            self.set_status(403, 'Forbidden')
            return self.finish({'message': 'Please Login', 'success': False})
        return method(self, *args, **kwargs)
    return wrapper


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(obj.timestamp() * 1000)
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        if isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        if isinstance(obj, datetime.timedelta):
            return obj.total_seconds()
        if isinstance(obj, decimal.Decimal):
            return float(obj)  # format(obj, 'f')
        # if isinstance(obj, Record):
        #     return dict(obj.items())
        return super().default(obj)


class BaseHandler(RequestHandler):
    _json = None
    _pageSize = None
    _pageStart = None

    @property
    def pageSize(self):
        if self._pageSize is None:
            self._pageSize = int(self.get_query_argument('pageSize', '20'))
        return self._pageSize

    @property
    def pageStart(self):
        if self._pageStart is None:
            current = int(self.get_query_argument('currentPage', '1'))
            self._pageStart = self.pageSize * (current - 1)
        return self._pageStart

    @property
    def json(self):
        return self._json

    @property
    def db(self):
        return self.application.settings['db']

    async def prepare(self):
        if self.request.body and self.request.headers.get('Content-Type', '').lower().startswith('application/json'):
            self._json = json.loads(self.request.body)
        uid = self.get_secure_cookie('uid')
        if uid:
            self.current_user = await self.db.fetchone('SELECT * FROM users WHERE uid=%s;', [uid,])
        if self.application.settings['debug']:
            app_log.warning(F'''
                url: {self.request.uri}
                uid cookie: {self.get_cookie('uid')}
                uid: {uid}, body: {self.request.body}
            ''')

    def check_xsrf_cookie(self) -> None:
        pass

    def success(self, data: Union[Dict, Collection, str] = None, message: str = None):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        return self.finish(json.dumps({'success': True, 'data': data, 'message': message}, cls=JSONEncoder, ensure_ascii=False))

    def failed(self, message: str = None, data: Any = None):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        return self.finish(json.dumps({'success': False, 'data': data, 'message': message}, cls=JSONEncoder, ensure_ascii=False))


class LoginHandler(BaseHandler):
    INVITE_COMMON_SCORE = 100  # 普通用户邀请成功获得100积分
    INVITE_PRO_SCORE = 500  # 特殊用户邀请成功获得500积分
    INVITED_USER_SCORE = 100  # 受邀者获得100积分。
    """/api/login
    打开App之后，自动登录，生成uuid
    保存用户信息、uuid等信息
    记录登录信息，如登录用户、登录时间
    根据访问的链接，记录受邀信息。

    邀请链接
    分为两种，普通邀请链接，专有邀请链接，
        邀请好友获得积分，不是金币。特殊用户邀请成功获得500积分，普通用户邀请成功获得100积分。受邀者获得100积分。
    受邀用户点击邀请链接
    打开App，生成登录信息，为受邀成功。

    {
        "inviter": null, // tid, not or uid string
        id: 12334, // int, required
        first_name,
    }
    """
    async def post(self):
        body, inviter_id, inviter = self.json, self.get_query_argument('inviter', None), None
        tid = body.get('id') if body else None
        if not tid:
            return self.failed('user id is required...')
        user = await self.db.fetchone('''
            SELECT * FROM users WHERE tid=%s;
        ''', [tid,])
        if user is not None:
            await self.db.execute('''
                -- need to record user login ?
                INSERT INTO user_logins (uid, ip) VALUES (%s, %s);
                UPDATE users
                    SET first_name=%s, last_name=%s, username=%s, language_code=%s, is_premium=%s
                    WHERE uid=%s;
            ''', [
                user['uid'], self.request.remote_ip,
                body['first_name'], body.get('last_name'), body.get('username'), body.get('language_code'), body.get('is_premium'),
                user['uid'],
            ])
            self.set_secure_cookie('uid', user['uid'])
            return self.success(user)
        if inviter_id:
            inviter = await self.db.fetchone('''
                SELECT * FROM users where tid=%s;
            ''', [inviter_id, ])
        # if wrong inviter, ignore it.
        uid = uuid.uuid4().hex
        sql_query, sql_args = '''
            INSERT INTO users
                (tid, uid, first_name, last_name, username, language_code, is_premium, inviter)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            INSERT INTO user_logins (uid, ip) VALUES (%s, %s);
        ''', [
            body['id'], uid, body['first_name'], body.get('last_name'), body.get('username'), body.get('language_code'), body.get('is_premium'),
            inviter['tid'] if inviter else None,  # inviter
            uid, self.request.remote_ip,
        ]
        if inviter is not None:
            inviter_score = self.INVITE_PRO_SCORE if inviter['invite_type'] == 'pro' else self.INVITE_COMMON_SCORE
            # if inviter['invite_type'] == 'pro':
            #     ''' 100 score '''
            sql_query += '''
                UPDATE users SET score=score+%s WHERE uid=%s;
                UPDATE users SET score=score+%s WHERE uid=%s;
                INSERT INTO users_scores
                    (uid, score, by_type, invite_uid)
                    VALUES(%s, %s, 'invite', %s);
            '''
            sql_args += [
                self.INVITED_USER_SCORE, uid,
                inviter_score, inviter['uid'],
                inviter['uid'], inviter_score, uid,
            ]
            # else:
            #     ''' 100 gold '''
            #     sql_query += '''
            #         UPDATE users SET gold=gold+100 WHERE uid=%s;
            #         INSERT INTO users_golds
            #             (uid, gold, by_type, invite_uid)
            #             VALUES(%s, 100, 'invite', %s);
            #     '''
            #     sql_args += [
            #         inviter['uid'],
            #         inviter['uid'], uid,
            #     ]
        await self.db.execute(sql_query, sql_args)
        user = await self.db.fetchone('''
            SELECT * FROM users WHERE tid=%s;
        ''', [tid,])
        self.set_secure_cookie('uid', user['uid'])
        return self.success(user)


class FriendsHandler(BaseHandler):
    """"/api/friends

    显示受邀好友数，积分，金币列表
    """
    @authenticated
    async def get(self):
        user = self.current_user
        # user = await self.db.fechone('SELECT * FROM users WHERE uid=%s;', [self.current_user['tid']])
        users = await self.db.fetchall('''
            SELECT * FROM users WHERE inviter=%s;
        ''', [user['tid'],])
        golds = await self.db.fetchall('''
            SELECT * FROM users_golds WHERE by_type=%s AND uid=%s;
        ''', ['invite', user['uid'],])
        scores = await self.db.fetchall('''
            SELECT * FROM users_scores WHERE by_type=%s AND uid=%s;
        ''', ['invite', user['uid'],])
        return self.success({'golds': golds, 'scores': scores, 'friends': users})


class UserHandler(BaseHandler):
    """/api/user

    显示账户信息：用户名、积分余额、uuid
    """
    @authenticated
    async def get(self):
        user = self.current_user
        today = None
        if self.get_query_argument('today', 'false') == 'true':
            today = {
                'gold': (await self.db.fetchone('''
                    SELECT SUM(gold) AS total FROM users_golds WHERE uid=%s AND DATE(create_time)=CURDATE();
                ''', [user['uid']]))['total'] or 0,
                'score': (await self.db.fetchone('''
                    SELECT SUM(score) AS total FROM users_scores WHERE uid=%s AND DATE(create_time)=CURDATE();
                ''', [user['uid']]))['total'] or 0,
            }
        return self.success({'user': user, 'today': today})

