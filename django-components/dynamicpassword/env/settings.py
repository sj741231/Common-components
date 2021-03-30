"""
 配置文件中需要修改的内容
"""

# 配置认证方式优先级，先LDAP,后本地认证
AUTHENTICATION_BACKENDS = (
    'accounts.hcssoauth.HCSSO_Auth',  # hcsso 登录认证
    'accounts.dynamicpassword.DynamicPassword_Auth',  # 本地密码 + hcsso 动态口令登录认证
    # 'django_crowd_auth.backends.Backend',                #django_crowd_auth模块认证，支持sso认证token+ip认证方式
    # 'accounts.crowdauth.CrowdAuth',                     #Crowd集中认证 ，自定义认证模块，有django_crowd_auth模块，可以不使用了
    # 'django_auth_ldap.backend.LDAPBackend',             #LDAP集中认证，暂时不再使用
    # 'django.contrib.auth.backends.ModelBackend',          # django 默认 账号 密码验证方式
    # 'django.contrib.auth.backends.RemoteUserBackend',   不能获取REMOTE_USER
)


# ENV = 'Production'
ENV = 'Testing'
########## SSO API   ##########
if ENV == 'Testing':
    SSOServerDomain = "http://authtest.hengchang6.com"  # 请修改为http://10.150.27.163
    SSOAccountDomain = 'http://10.150.26.29:8000'
elif ENV == 'Production':
    SSOServerDomain = "http://auth.hengchang6.com"  # 生产
    SSOAccountDomain = 'http://10.10.255.196'  # 生产

SSOClientDomain = "http://172.30.12.142:9090"  # 请修改为您项目的根域名  nginx uwsgi

APPKEY = "testkey"  # 请修改为您项目对应的key

SSOauthURL = SSOServerDomain + "/authorize?appkey=" + APPKEY + "&returnurl=" + SSOClientDomain + "/accounts/login"

# LOGIN_EXEMPT_URLS = ["dologout", "test", "dotest"]  ##拦截器中间件例外

VERIFY_ACCOUNTS_URL = SSOAccountDomain + '/api/v1/user/query?'  # SSO 获取账号信息
GET_DEPARTMENT_URL = SSOAccountDomain + '/api/v1/department/get?'  # SSO 获取部门信息
GET_ACCESS_TOKEN_URL = SSOServerDomain + '/getaccesstoken'  # 获得access token
GET_USER_INFO_URL = SSOServerDomain + '/getuserinfo'  # 获取用户信息, SSO登录使用
DO_LOGOUT_URL = SSOServerDomain + '/dologout'  # SSO 登出
VALIDATE_SECRET_URL = SSOServerDomain + '/api/v1/validatesecret'  # 动态口令验证接口

SSO_API_URL = {
    'VERIFY_ACCOUNTS': {'url': VERIFY_ACCOUNTS_URL,
                        'method': 'GET',
                        'params': ('object',)},
    'GET_DEPARTMENT': {'url': GET_DEPARTMENT_URL,
                       'method': 'GET',
                       'params': ('id',)},
    'GET_ACCESS_TOKEN': {'url': GET_ACCESS_TOKEN_URL,
                         'method': 'POST',
                         'params': ('appkey', 'auth_code')},
    'GET_USER_INFO': {'url': GET_USER_INFO_URL,
                      'method': 'POST',
                      'params': ('access_token', 'sessionid')},
    'LOGOUT_URL': {'url': DO_LOGOUT_URL,
                   'method': 'POST',
                   'params': ('access_token', 'sessionid')},
    'VALIDATE_SECRET': {'url': VALIDATE_SECRET_URL,
                        'method': 'POST',
                        'params': ('access_token', 'sessionid'),
                        'enable': True,
                        'default_account': 'shijin170714@credithc.com'}
}


