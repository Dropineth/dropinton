import os
import json
import hashlib

import shutil

import pymysql
import pymysql.cursors

mysql_config_file = os.path.join(os.path.dirname(__file__), 'mysql.local.json')
if os.path.exists(mysql_config_file):
    with open(mysql_config_file) as fd:
        mysql_config = json.load(fd)
    print('database: %(user)s:********@%(host)s:%(port)s?db=%(db)s' % mysql_config)
else:
    print('***** mysql.local.json need *****')
    exit(0)

def main():
    DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'web-vant/public/img/cards/'))
    connection = pymysql.connect(**mysql_config, autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from cards;')
    cards = cursor.fetchall()
    for card in cards:
        urls, img = {}, card["img"]
        for status in ('blink', 'gray', 'unknown'):
            _file = os.path.join(DIR, F'{status}-{img}.png')
            if os.path.exists(_file):
                with open(_file, 'rb') as f:
                    body = f.read()
                    md5_10 = hashlib.md5(body).hexdigest()[12:22]
                    urls[status] = F'{img}-{status}-{md5_10}.png'
                    shutil.copy(_file, os.path.join(DIR, urls[status]))
        print('img', img, urls)
        cursor.execute('UPDATE cards SET urls=%s WHERE id=%s;', [json.dumps(urls), card['id']])
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
    # 更新卡片 url，刷数据库 删除字段 url, coming_img, 增加 urls 字段(json 类型)
    # python md5-cards-img.py

#######################################################################################
# web-vant/public/img/cards 存放的重命名后的文件，原始文件不要上传，这里 gitignore
# web-vant/public/img/_cards 存放的是原始文件，通过此脚本重命名后复制到 cards 目录，对外提供url
#######################################################################################