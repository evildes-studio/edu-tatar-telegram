from bs4 import BeautifulSoup
import logging
from requests.sessions import Session
import datetime


class Parser:
    USER_DATA = {"name": "имя", "school": "школа", "position": "должность", "b_day": "дата рождения", "gender": "пол",
                 "pupil_id": "номер сертификата", "mail": "личная почта пользователя"}

    def __init__(self, session: Session):
        """
        Parser for edu.tatar.ru
        :param session: edu.tatar.ru' requests session object
        """
        self.session = session
        self.user_info = {}

    def get_user_info(self, keys: list = None) -> [dict, list]:
        """
        Returns all info about user (edu.tatar.ru' cabinet)
        :param keys: by certain keys (defined in self.USER_DATA)
        :return: info from the user's cabinet
        """
        if not self.user_info:
            result = self.session.get("https://edu.tatar.ru/user/anketa")
            html = BeautifulSoup(result.content, 'html.parser')

            for item in html.select('#cabinet .tableEx tr'):
                info_field = item.find("td")
                field_text = info_field.get_text().strip().rstrip(":").lower()

                if field_text in self.USER_DATA.values():
                    sibling_text = info_field.find_next_sibling("td").get_text().strip()
                    self.user_info[get_dict_key(self.USER_DATA, field_text)] = sibling_text

        if keys:
            temp = {}
            for key in keys:
                temp[key] = self.user_info[key]
            return list(temp.values())

        return self.user_info

    def get_marks(self, subject: str = None, term: int = None, date: str = None,
                  limit: int = -1, mark_info: bool = False, clear_null: bool = False) -> [list, int]:
        """
        Returns all marks
        :param subject: by certain subject name
        :param term: by term
        :param date: by date
        :param limit: limit output
        :param mark_info: show the mark info (such a subject name, teacher name, etc.)
        :param clear_null: clear empty objects
        :return: list of marks
        """
        base_url = "https://edu.tatar.ru/user/diary/"
        marks = []

        if date:
            date_ = datetime.datetime.strptime(date, "%d.%m.%Y")
            timestamp = datetime.datetime.timestamp(date_)

            result = self.session.get(base_url + f"day?for={timestamp}")
            html = BeautifulSoup(result.content, 'html.parser')

            for item in html.select("#content .xdiary .d-table > .main tbody > tr"):
                marks_block = item.select("table.marks tr td")
                marks_ = [{"title": i.get('title').strip(), "value": float(i.get_text().strip())} for i in marks_block]
                subject_name = item.find_all("td")[1].get_text().strip()

                object_ = {
                    "subject": subject_name,
                    "marks": marks_
                }

                if subject_name.lower() == subject.lower():
                    marks.append(object_)
                    break
                elif subject:
                    continue
                else:
                    marks.append(object_)

        if not date and term:
            result = self.session.post(base_url + "term", data={"term": term})
            html = BeautifulSoup(result.content, 'html.parser')

            for item in html.select("#content .term-marks tbody tr"):
                subject_name = item.find_all("td")[0].get_text().strip()
                marks_ = []

                for mark in item.find_all("td")[1:-3]:
                    mark_ = mark.get_text().strip()
                    if mark_.isdigit():
                        marks_.append(float(mark_))

                object_ = {
                    "subject": subject_name,
                    "marks": marks_
                }

                if subject_name.lower() == subject.lower():
                    marks.append(object_)
                    break
                elif subject:
                    continue
                else:
                    marks.append(object_)

        if not mark_info:
            for i, item in enumerate(marks):
                marks_ = list(map(lambda x: x['value'], item['marks']))
                marks[i] = marks_

        if clear_null:
            temp = []
            for i, item in enumerate(marks):
                if not item:
                    continue
                try:
                    if item['marks']:
                        temp.append(item)
                except TypeError:
                    temp.append(item)
            marks = temp

        logging.debug(f"[!] Got marks from {'term' if term else 'date'}: {marks[:limit]}")
        return marks[:limit]


def get_dict_key(dict_, value):
    for x in dict_.keys():
        if dict_[x] == value:
            return x
    return None
