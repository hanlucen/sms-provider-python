'''
Created on 2016年11月10日

@author: hanlucen
'''
import unittest
from sms_provider.provider import YunXinProvider
YUNXIN_DOMAIN = 'http://xxx'
USER_CODE = 'xxx'
USER_PASS = 'xxx'


class YunXinProviderTest(unittest.TestCase):

    def test_send_message(self):
        provider = YunXinProvider(YUNXIN_DOMAIN, USER_CODE, USER_PASS, '【xx】')
        provider.send_message(
            '13333333333',
            message='123456（验证码），10分钟内有效，你正在绑定手机号。',
            use_async=False)


if __name__ == '__main__':
    unittest.main()
