'''
Created on 2016年11月10日

@author: hanlucen
'''
import requests
import logging
import xml.etree.ElementTree as ET
import threading


logger = logging.getLogger('default')


class Provider:

    def __init__(self, domain='', username='', password='', app=''):
        self.domain = domain
        self.username = username
        self.password = password
        self.app = app

    def send_message(self):
        pass


class YiMeiProvider(Provider):

    def __init__(self, domain, username, password, app):
        Provider.__init__(self, domain, username, password)

    def send_message(self):
        pass


class YunXinProvider(Provider):

    def __init__(self, domain, username, password, app):
        Provider.__init__(self, domain, username, password, app)

    def send_message(self, receiver, message='', use_async=False):
        data = {
            "userCode": self.username,
            "userPass": self.password,
            "DesNo": receiver,
            "Msg": '%s%s' % (message, self.app),
            "Channel": 0
            }
        if use_async:
            threading.Thread(target=self._send, args=[data]).start()
        else:
            self._send(data)

    def _send(self, data):
        try:
            resp = requests.post(self.domain, data=data)
        except requests.exceptions.ConnectionError or \
                requests.exceptions.Timeout as e:
            logger.error(e)
            return
        if resp.status_code == 200:
            result = resp.text.strip()
            logger.info('data: %s, response: %s' % (data, result))
            result = ET.fromstring(result)
            status_code = int(result.text)
            if status_code <= 0:
                logger.error(
                    'send message fail, receiver:%s, code:%s, msg:%s' % (
                        data['DesNo'], status_code, data['Msg']))
        else:
            logger.error('send message fail')
