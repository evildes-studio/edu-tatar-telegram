from bs4 import BeautifulSoup
import requests
import logging


class Parser:
    USER_DATA = {"name": "имя", "school": "школа", "position": "должность", "b_day": "дата рождения", "gender": "пол",
                 "pupil_id": "номер сертификата", "mail": "личная почта пользователя"}

    def __init__(self, session):
        self.session = session
        self.user_info = {}

    def get_user_info(self, keys=None):
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


def get_dict_key(dict_, value):
    for x in dict_.keys():
        if dict_[x] == value:
            return x
    return None
