import re


class HTMLTextParser:

    def __init__(self):
        self._href_regex = re.compile(r'<a.*>.*</a>')
        self._href_link_regex = re.compile(r'href=".*?"')
        self._text_tags = [r'<p.*?>', r'</p>', r'<title>', 'r</title>'] #Нужен ленивый захват, иначе хапает всё
        # до конца строки
        self._regex_text_tags = re.compile('|'.join(self._text_tags))
        # Нужен ленивый захват, иначе хватает лишнее справа (в имени класса, например)

    def generate_readability_text(self, graped_html_text_data, text_width: int = 80):
        """graped_html_text_data - list of html strings."""
        graped_html_text_data = self.replace_html_tags(graped_html_text_data)
        text = self.generate_text_by_data(graped_html_text_data)

        # 1) Замена ссылок
        # 2) Ширина не больше заданного параметра. Перенос по словам
        # 3) абзацы и заголовки отбиваются пустой строкой. (<p> и <title>)
        # 4) Остальные правила на ваше усмотрение.
        pass

    def replace_html_tags(self, html_text_data):
        """html_text_data - list of html strings."""
        for index, value in enumerate(html_text_data):
            html_text_data[index] = self.__delete_text_tags(self.__replace_href(value))
        return html_text_data

    def __replace_href(self, text_entry):
        for href in re.findall(self._href_regex, text_entry):
            href_link = re.findall(self._href_link_regex, href)
            if len(href_link) > 0:
                new_link = '[{}]'.format(href_link[0].replace('href=', '').replace('"', ''))
                text_entry = text_entry.replace(href, new_link, 1)
                # может что получше придумать, а то каждый раз строка создается (неизменяемый тип)
        return text_entry

    def __delete_text_tags(self, text_entry):
        return re.sub(self._regex_text_tags, '', text_entry)

    def generate_text_by_data(self, html_text_data, text_width: int = 80):
        """html_text_data - list of html strings."""
        text_with_offsets = "\n".join(html_text_data)
