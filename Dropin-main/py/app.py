import os
import json
import asyncio

from tornado.web import RequestHandler, Application
from tornado.options import define, options, parse_command_line
from tornado.log import app_log
from tornado.httpserver import HTTPServer

# app_config_file = __file__.replace('app.py', 'app.local.json')
# if os.path.exists(app_config_file):
#     with open(app_config_file) as fd:
#         app_config = json.load(fd)
#     app_log.warning('app config: %s', app_config)
# else:
#     app_demo_file = __file__.replace('app.py', 'app.json')
#     app_log.error('*****\n'
#         F'1. app.local.json need, copy from {app_demo_file} and edit it.\n'
#         '2. restart command: python app.py --port=16666 --debug=false\n'
#     '*****')
#     exit(0)

mysql_config_file = __file__.replace('app.py', 'mysql.local.json')
if os.path.exists(mysql_config_file):
    with open(mysql_config_file) as fd:
        mysql_config = json.load(fd)
    app_log.warning('database: %(user)s:********@%(host)s:%(port)s?db=%(db)s', mysql_config)
else:
    mysql_demo_file = __file__.replace('app.py', 'mysql.json')
    app_log.error('*****\n'
        F'1. mysql.local.json need, copy from {mysql_demo_file} and edit it.\n'
        '2. restart command: python app.py --port=16666 --debug=false\n'
    '*****')
    exit(0)

from util.mysql_pool import create_pool
from py import base, wallet
# from py import twitter as tw
# from py import twitter2 as tw

# dev default 18888, pro 16666
define("port", default=18888, type=int, help="listen port")
define("debug", default="true", type=bool, help="debug mode")


def json_encode(value: dict) -> str:
    return json.dumps(value, cls=base.JSONEncoder, ensure_ascii=False)


import tornado.escape
tornado.escape.json_encode = json_encode


class MainHandler(RequestHandler):
    def get(self):
        self.finish("Hello Python!")


class ConfigHandler(RequestHandler):
    async def get(self):
        configs = await self.application.settings['db'].fetchall('''
            SELECT * FROM internal_configs WHERE `key` IN ('web', 'ton', 'game');
        ''')
        config_dict = dict((c['key'], c['value']) for c in configs)
        web_config = config_dict['web']
        web_config['ton'] = config_dict['ton']
        # web_config['game'] = config_dict['game']
        self.finish(web_config)


class ToDoHandler(RequestHandler):
    async def get(self):
        print('TODO: json_schema...')
        app_log.info('full_url: %s', self.request.full_url())
        self.finish("ToDo ...")


async def main():
    db = await create_pool(mysql_config)
    # twitter_config = await db.fetchone('SELECT `value` FROM internal_configs WHERE `key`=%s;', ['ton',])
    app = Application([
        (r"/", MainHandler),
        (r"/api/todo", ToDoHandler),
        (r"/api/config", ConfigHandler),
        (r"/api/login", base.LoginHandler),  # post
        (r"/api/user", base.UserHandler),  # get
        # (r"/api/user/cards", base.UserCardsHandler),  # get
        (r"/api/friends", base.FriendsHandler),  # post
        (r"/api/wallet/update", wallet.WalletSaveHandler),  # post
    ],
        xsrf_cookies=False,
        cookie_secret='sheep_2024',  # datetime.today().strftime("sheep%Y%m%d"),
        debug=options.debug,
        autoreload=True,
        template_path=__file__.replace('app.py', 'templates'),
        # **twitter_config['value'],
    )
    app.settings['db'] = db
    server: HTTPServer = app.listen(options.port, xheaders=True)
    app_log.warning("tornado start at port: %s, debug: %s", options.port, options.debug,)
    await asyncio.Event().wait()


if __name__ == "__main__":
    parse_command_line()
    asyncio.run(main())
    # 开发启动 python app.py
    # 正式启动 python app.py --port=16666 --debug=false
    # 宝塔启动 1. 选择 python 启动（不使用任何框架），2. 启动参数： --port=16666 --debug=false
    # 清理个人任务数据：python py/twitter2_clear.py c51a629e6afb4604a09925b05a4dee6c
