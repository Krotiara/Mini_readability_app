# coding:cp1252
from App import TextGenerator
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--article_url', '-url', help="URL address of article", type=str)
    parser.add_argument('--settings', '-s', help="parser settings file", type=str)
    parser.add_argument('--text_width', '-w', help="parser line width", type=int)
    args = parser.parse_args()
    tags_to_search = ['title', 'p', 'h']
    text_width = 80
    if args.settings is not None:
        settings_dict = TextGenerator.TextGenerator.read_settings(args.settings)
        tags_to_search = settings_dict['searching_tags'].split(',')
        text_width = int(settings_dict['text_width'])
    if args.text_width is not None:
        text_width = int(args.text_width)
    TextGenerator.TextGenerator.generate_readability_text(args.article_url, text_width, tags_to_search)
