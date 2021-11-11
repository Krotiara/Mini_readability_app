import re
import App.CustomExceptions
import html


class HTMLTextParser:

    def __init__(self):
        self._href_regex = re.compile(r'<a.*?>.*</a>')
        self._image_regex = re.compile(r'<img.*?>')
        self._href_link_regex = re.compile(r'href=".*?"')
        self._image_link_regex = re.compile(r'src=".*?"')
        self._all_tags_regex = re.compile('|'.join([r'<.*?>.*</.*?>',r'<.*?>']))
        self._replace_tags = [r'<p.*?>', r'</p>', r'<title>', r'</title>',
                              r'<h\d.*?>', r'</h\d>', r'<span.*?>',
                              r'</span>']  # Нужен ленивый захват, иначе хапает всё
        # до конца строки
        self._regex_replace_tags = re.compile('|'.join(self._replace_tags))
        # Нужен ленивый захват, иначе хватает лишнее справа (в имени класса, например)

    def generate_readability_text(self, graped_html_text_data, text_width: int = 80):
        """graped_html_text_data - list of html strings."""
        raw_text = "\n\n".join(graped_html_text_data)  # отбивка новой строкой
        text = self.replace_tags(raw_text)
        text = html.unescape(self.__delete_tags_by_regex(text, self._regex_replace_tags))
        text = self.__delete_tags_by_regex(text, self._all_tags_regex) #Очищаем случайно попавшие
        # Если нельзя html.unescape, то определить словарь замен entities
        result_text = self.adjust_text_by_width(text, text_width)
        return result_text

    def replace_tags(self,text):
        text = self.__replace_tag_by_local_part(text, self._href_regex, self._href_link_regex, '[{}]',
                                                ['href=', '"'])
        text = self.__replace_tag_by_local_part(text, self._image_regex,self._image_link_regex, '[Source: {}]',
                                                ['src=','"'])
        return text

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
                        word_chunks = self.adjust_long_word(word, text_width)
                        generated_text += "\n".join(word_chunks)
                        current_line_items.clear()
                        current_width = len(word_chunks[-1])
                        #raise App.CustomExceptions.TextWidthException(text_width, current_width,word)
            if len(current_line_items) > 0:
                generated_text += " ".join(current_line_items)
            generated_text += '\n'  # Восстановление переноса, по которому сплитились
        return generated_text

    def adjust_long_word(self, word, text_width): #Это не умный переносчик.
        chunks = [word[i:i + text_width] for i in range(0, len(word), text_width)]
        return chunks

#Переделать под универсальный?
    def __replace_tag_by_local_part(self, text:str, regex, local_regex, replacement, replacement_empty):
        for tag in re.findall(regex, text):
            local_part = re.findall(local_regex, tag)
            if len(local_part) > 0:
                new_tag = replacement.format(*local_part)
                for entry in replacement_empty:
                    new_tag = new_tag.replace(entry,'')
                text = text.replace(tag, new_tag)
        return  text



    def __replace_href(self, text_entry):
        for href in re.findall(self._href_regex, text_entry):
            href_link = re.findall(self._href_link_regex, href)
            if len(href_link) > 0:
                new_link = '[{}]'.format(href_link[0].replace('href=', '').replace('"', ''))
                text_entry = text_entry.replace(href, new_link, 1)
                # может что получше придумать, а то каждый раз строка создается (неизменяемый тип)
        return text_entry

    def __delete_tags_by_regex(self, text:str, regex):
        return re.sub(regex,'',text)
