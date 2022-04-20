import requests
import random
from configparser import ConfigParser
import logging

config = ConfigParser()
config.read('config/config.ini', encoding="utf8")


class EduTatar:
    def __init__(self):
        self.login = None
        self.password = None

        self.name = None
        self.surname = None
        self.grade = None
        self.pupil_id = None

        self.session = None
        self.parser = None

        self.auth()

    def auth(self):
        session = requests.Session()
        user_agent = GET_UA()
        session.get(config['edu_tatar']['url_login'], headers={
            'User-Agent': user_agent
        })
        session.headers.update({'Referer': config['edu_tatar']['url_login']})
        session.headers.update({'User-Agent': user_agent})
        _xsrf = session.cookies.get('_xsrf', domain=".tatar.ru")
        s = session.post(config['edu_tatar']['url_login'],
                         {
                             config['edu_tatar']['login_name']: self.login,
                             config['edu_tatar']['password_name']: self.password
                         })
        logging.info(s)
        logging.info(s.text)
        logging.info(s.content)

        self.session = session
        return session


def GET_UA():
    ua_strings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 "
        "Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 "
        "Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 "
        "Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
    ]

    return random.choice(ua_strings)
