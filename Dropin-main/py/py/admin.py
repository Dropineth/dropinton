import json
import time
from tornado.web import RequestHandler

from py.base import authenticated, BaseHandler


import uuid
import string


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

class LoginHandler(RequestHandler):
    def post(self):
        """30分钟过期，重新登录好了，没必要退出了；"""
        if self.get_body_argument('password') == 'schwarzkopf_admin':
            self.set_secure_cookie('schwarzkopf_admin', F'{time.time():0.0f}', None, httponly=True)
            return self.finish({'success': True, 'message': '登录成功'})
        return self.finish({'success': False, 'message': '登录失败'})


# class LogoutHandler(RequestHandler):
#     def post(self):
#         pass


class AdminBaseHandler(BaseHandler):
    def prepare(self):
        if self.request.body and self.request.headers.get('Content-Type', '').lower().startswith('application/json'):
            self._json = json.loads(self.request.body)
        timestamp = self.get_secure_cookie('schwarzkopf_admin')
        if (not timestamp) or (time.time() - int(timestamp) > 3600 * 24):
            print('timestamp', timestamp)
            self.set_status(401)
            return self.failed(msg='请登录')
        self.current_user = {'timestamp': timestamp}


class ShopsHandler(AdminBaseHandler):
    @authenticated
    async def get(self):
        shops = await self.db.fetchall(F'''SELECT * FROM shops ORDER BY id ASC;''', )
        return self.success({'shops': shops})


class ShopDatesHandler(AdminBaseHandler):
    """get 门店预约可用日期
    post 门店预约
    """
    @authenticated
    async def get(self):
        shop_id = self.get_query_argument('shop_id', None)
        where_sql, where_args = [], []
        if shop_id:
            where_sql.append(F'a.shop_id=%s')
            where_args.append(shop_id)
        result = await self.db.fetchall(F'''
            SELECT a.open_id, a.date, TIME_FORMAT(a.time, '%%H:%%i') AS `time`, a.name, a.phone, a.create_time
            FROM appointments a
            {('WHERE ' + ' AND '.join(where_sql)) if where_sql else ''}
            ORDER BY a.shop_id ASC, a.date ASC, a.time ASC, a.create_time ASC;
        ''', where_args)
        return self.success({'appointments': result})

    @authenticated
    async def delete(self):
        open_id = self.get_query_argument('open_id')
        result = await self.db.fetchall(F'''
            DELETE FROM appointments a
            WHERE open_id=%s;
        ''', (open_id,))
        return self.success(msg='删除成功')

