import re


class HTMLTextParser:

    def __init__(self):
        self._href_regex = re.compile(r'<a.*>.*</a>')
        self._href_link_regex = re.compile(r'href=".*?"')
        self._text_tags = [r'<p.*?>', r'</p>', r'<title>', 'r</title>']  # Нужен ленивый захват, иначе хапает всё
        # до конца строки
        self._regex_text_tags = re.compile('|'.join(self._text_tags))
        # Нужен ленивый захват, иначе хватает лишнее справа (в имени класса, например)

    def generate_readability_text(self, graped_html_text_data, text_width: int = 80):
        """graped_html_text_data - list of html strings."""
        self.replace_html_tags(graped_html_text_data)
        result_text = self.adjust_text_by_width("\n".join(graped_html_text_data), text_width)
        return result_text

        # 1) Замена ссылок done
        # 2) Ширина не больше заданного параметра. Перенос по словам done
        # 3) абзацы и заголовки отбиваются пустой строкой. (<p> и <title>) done
        # 4) Остальные правила на ваше усмотрение.
        pass

    def replace_html_tags(self, html_text_data):
        """html_text_data - list of html strings."""
        for index, value in enumerate(html_text_data):
            html_text_data[index] = self.__delete_text_tags(self.__replace_href(value))

    def adjust_text_by_width(self, text, text_width: int = 80):
        generated_text = ''
        for line in text.split("\n"):
            current_width = 0
            current_line_items = []
            for word in line.split():
                potential_width = len(word) + current_width + 1  # +1 - учет пробела
                if potential_width < text_width:
                    current_line_items.append(word)
                    current_width = potential_width
                else:
                    generated_text += " ".join(current_line_items) + "\n"
                    current_line_items.clear()
                    current_line_items.append(word)
                    current_width = len(word)
                    if current_width > text_width:
                        raise Exception("There are words in text which length is larger"
                                        " than input text_width param = {}".format(text_width))
            if len(current_line_items) > 0:
                generated_text += " ".join(current_line_items)
            generated_text += '\n'  # Восстановление переноса, по которому сплитились
        return generated_text

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
