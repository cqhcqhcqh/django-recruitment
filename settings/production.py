# 先将 base 配置全部导入进来
from .base import *

# 然后覆盖 base 中的一部分配置来实现 local 中配置的差异化
# 生产环境的 ALLOWED_HOSTS，只允许 127.0.0.1
# 通常在生产环境，我们会把可访问地址通过 Nginx 或者其他网关给它代理出去
# 而不是直接填写服务器的地址 eg. `10.147.18.212`
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DEBUG = False