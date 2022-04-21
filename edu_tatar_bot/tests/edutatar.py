import unittest
from edu_tatar_bot.classes.EduTatar import EduTatar
from requests.sessions import Session
import logging
import json
import os


class TestEduTatar(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        with open(os.getcwd() + '\\tests\\test_data.json') as f:
            self.test_data = json.load(f)
            logging.info('[!] Test Data is loaded!')

    def test_auth(self):
        edu_tatar = EduTatar(login=self.test_data["edu_login"], password=self.test_data["edu_password"])
        self.assertEqual(type(edu_tatar.auth()), Session)

    def test_proxy_auth(self):
        edu_tatar = EduTatar(login=self.test_data["edu_login"], password=self.test_data["edu_password"],
                             proxy=self.test_data["proxy"])
        self.assertEqual(type(edu_tatar.auth()), Session)


if __name__ == '__main__':
    unittest.main()
