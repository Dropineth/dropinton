# 使用宝塔安装即可(网页操作, 11版本)

## 部署选择 python，别忘记添加启动参数

WEB 部署：/www/wwwroot/MiniApp/sheep-dev
Python 部署：/www/wwwroot/MiniApp/sheep-dev-py
Python 日志：/www/wwwlogs/python/sheep-dev-py/error.log

### 宝塔伪静态配置
```conf
# 请将伪静态规则或自定义NGINX配置填写到此处
location ^~ /api {
    proxy_set_header Host $host;
    proxy_set_header X-Real-Ip $remote_addr;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_pass   http://127.0.0.1:16666;
}
```