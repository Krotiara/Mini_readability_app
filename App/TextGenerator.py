from App import TextWriter as TW
from App import WebPagesHandler as WH
from App import HTMLTextParser as HP
import os


class TextGenerator:

    @staticmethod
    def generate_readability_text(url: str, text_width: int = 80,
                                  tags_to_search=None):
        web_parser = WH.WebPagesParser()
        html_parser = HP.HTMLTextParser()
        text_writer = TW.TextWriter()
        text = html_parser.generate_readability_text(
            web_parser.get_html_data(url, tags_to_search), text_width)
        text_writer.write_by_url_format(text, url)
        return text

    @staticmethod
    def read_settings(settings_file_name):
        """read text generator settings from local file"""
        settings_dict = {}
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = '{}/Settings/{}'.format(os.path.dirname(current_dir), settings_file_name)
        print(path)
        with open(path, 'r', encoding='utf-8') as settings:
            for line in settings:
                (key, val) = line.split('=')
                settings_dict[key] = val
        return settings_dict
