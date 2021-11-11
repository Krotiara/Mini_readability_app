import requests
import re


class WebPagesParser:
    def __init__(self):
        self._regex_list = [r'<p.*?>.+?</p>', r'<title>.+?</title>', r'<h\d.*?>.+?</h\d>', r'<span.*?>.+?</span>']
        # + ~ не берем пустые body в тэгах

        self._combined_text_regex = re.compile('|'.join(self._regex_list))

    def get_html_data(self, url:str, regex=None):
        return self.grap_needed_html_data(self.get_url_text(url), regex)

    def grap_needed_html_data(self, html_text:str, regex=None):
        """Grap data by regex patterns. (Without Beautiful Soup).
        Output - list of founded tags strings"""
        if regex is None:
            regex = self._combined_text_regex
        parsed_data = re.findall(regex, html_text)
        return parsed_data

    @staticmethod
    def get_url_text(url):
        try:
            responce = requests.get(url)
            return responce.text
        except requests.ConnectionError as e:
            print(e) # заменить на уведомление


