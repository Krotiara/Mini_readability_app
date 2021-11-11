import os
from random import randint

class TextWriter:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.texts_dir = '{}/Texts'.format(os.path.dirname(self.current_dir))
        self.__check_texts_folder_exist(self.texts_dir)

    def __check_texts_folder_exist(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def write_by_url_format(self, text, url: str):
        url = url.replace('http://', '').replace('https://', '')
        split = url.split('/')
        if self.__is_file_name_exist(split):
            file_name = '{}.txt'.format(os.path.splitext(split[-1])[0])
            file_path = self.__get_text_path(split[:-1])
        else:
            file_name = '{}.txt'.format(randint(0, 100))
            file_path = self.__get_text_path(split)
        file_path = '{}/{}'.format(file_path, file_name)
        with open(file_path, 'w+',encoding="utf-8") as file:
            file.write(text)

    def __get_text_path(self, folders_hierarchy):
        current_path = self.texts_dir
        for folder in folders_hierarchy:
            new_path = '{}/{}'.format(current_path, folder)
            self.__check_texts_folder_exist(new_path)
            current_path = new_path
        return current_path

    def __is_file_name_exist(self, url_split):
        return os.path.splitext(url_split[-1])[0] != ''
