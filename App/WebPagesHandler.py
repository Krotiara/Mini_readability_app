import requests
import re


class WebPagesParser:
    def __init__(self):
        # + ~ не берем пустые body в тэгах
        self._regex_tag_dict = {'p': r'<p.*?>.+?</p>', 'title': r'<title>.+?</title>', 'h': r'<h\d.*?>.+?</h\d>',
                                'span': r'<span.*?>.+?</span>', 'img': r'<img.*?>'}
        self._combined_text_regex = re.compile('|'.join(self._regex_tag_dict.values()))

    def get_html_data(self, url: str, tags_to_search=None):
        return self.grap_needed_html_data(self.get_url_text(url),tags_to_search)

    def grap_needed_html_data(self, html_text: str, tags_to_search=None):
        """Grap data by regex patterns. (Without Beautiful Soup).
        tags_to_search - list of tags strings
        Output - list of founded tags strings"""
        self.set_regex_by_settings(tags_to_search)
        parsed_data = re.findall(self._combined_text_regex, html_text)
        return parsed_data

    def set_regex_by_settings(self, tags_to_search): #Обработка исключения
        if tags_to_search is not None:
            regex_list = []
            for tag in tags_to_search:
                regex_list.append(self._regex_tag_dict[tag])
            self._combined_text_regex = re.compile('|'.join(regex_list))

    @staticmethod
    def get_url_text(url):
        try:
            responce = requests.get(url)
            return responce.text
        except requests.ConnectionError as e:
            print(e)  # заменить на уведомление
