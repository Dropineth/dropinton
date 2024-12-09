import os
import json
# 不知道为什么高版本的 pymysql 不支持 json 字段了，旧版本代码有bug，自己实现
import pymysql.converters
import pymysql.constants.FIELD_TYPE

def escape_dict(val, charset, mapping=None):
    # n = {}
    # for k, v in val.items():
    #     quoted = pymysql.converters.escape_item(v, charset, mapping)
    #     n[k] = quoted
    # return n
    return F"'{pymysql.converters.escape_string(json.dumps(val, ensure_ascii=False))}'"


def convert_json(val):
    return json.loads(val)


pymysql.converters.__dict__['escape_dict'] = escape_dict
pymysql.converters.escape_dict = escape_dict
pymysql.converters.encoders[dict] = escape_dict
pymysql.converters.conversions[dict] = escape_dict
# 解码 pymysql.constants.FIELD_TYPE.JSON = 245
pymysql.converters.decoders[pymysql.constants.FIELD_TYPE.JSON] = convert_json
pymysql.converters.conversions[pymysql.constants.FIELD_TYPE.JSON] = convert_json


from aiomysql import create_pool as cp, DictCursor, Pool


def create_pool(kwargs):
    return cp(
        maxsize=20,
        charset="utf8mb4", autocommit=True,
        connect_timeout=10,  # 10秒超时
        cursorclass=DictCursor,
        **kwargs
    )


async def execute(self, query, args=None):
    async with self.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(query, args)
            if os.name == 'nt':
                print('SQL execute:', cur._executed)
            # return {'rowcount': cur.rowcount, 'insert_id': cur.lastrowid, 'rows': cur._rows}
            return cur


async def fetchone(self, query, args=None):
    async with self.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(query, args)
            if os.name == 'nt':
                print('SQL fetchone:', cur._executed)
            # item = await cur.fetchone()
            # print('fetchone:', cur._executed, '_result', cur._result, 'rows', cur._rows, 'id:', cur._lastrowid)
            # return item
            return await cur.fetchone()


async def fetchall(self, query, args=None):
    async with self.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(query, args)
            if os.name == 'nt':
                print('SQL fetchall:', cur._executed)
            return await cur.fetchall()


Pool.execute = execute
Pool.fetchall = fetchall
Pool.fetchone = fetchone
