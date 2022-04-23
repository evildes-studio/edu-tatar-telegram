import unittest
from edu_tatar_bot.classes.EduTatar import EduTatar
from edu_tatar_bot.classes.Parser import Parser
import logging
import json
import os


class TestParser(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        with open(os.getcwd() + '\\tests\\test_data.json', encoding="utf8") as f:
            self.test_data = json.load(f)
            logging.info('[!] Test Data is loaded!')

        edu_tatar = EduTatar(login=self.test_data["edu_login"], password=self.test_data["edu_password"])
        self.session = edu_tatar.auth()
        self.parser = Parser(session=self.session)

    def test_get_user_info(self):
        self.assertEqual(self.parser.get_user_info(keys=self.test_data["parser"]["get_user_info"]["keys"]),
                         self.test_data["parser"]["get_user_info"]["valid_data"])

    def test_get_marks(self):
        get_marks = self.test_data["parser"]["get_marks"]
        self.assertEqual(self.parser.get_marks(subject=get_marks["subject"], term=get_marks["term"],
                                               date=get_marks["date"], limit=get_marks["limit"],
                                               mark_info=get_marks["mark_info"],
                                               clear_null=get_marks["clear_null"]), get_marks["valid_data"])


if __name__ == '__main__':
    unittest.main()
