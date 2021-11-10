import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))
from App import WebPagesHandler as WPH
from  App import  HTMLTextParser as HTP


class Test(unittest.TestCase):
    def setUp(self):
        self.web_pages_handler = WPH.WebPagesParser()
        self.html_text_parser = HTP.HTMLTextParser()
        self.test_str = '<p>P tag without class</p>\nsimple text\n<p class="class1">P tag with class</p>\n' \
                        '<title>TITLE</title>\n<p class="hqeiq">blablabla. <a href="/tags/organizations/mid/" ' \
                        'target="_blank" class="hqgaw">МИД России</a></p>'

    def test_regex(self):
        parse_result = self.web_pages_handler.grap_needed_html_data(self.test_str)
        self.assertEqual(parse_result, ['<p>P tag without class</p>', '<p class="class1">P tag with class</p>',
                                        '<title>TITLE</title>',
                                        '<p class="hqeiq">blablabla. <a href="/tags/organizations/mid/" ' \
                                        'target="_blank" class="hqgaw">МИД России</a></p>'])

    def test_html_tags_replacement(self):
        test_data = ['<p class="hqeiq">blablabla. <a href="/tags/organizations/mid/" target="_blank" '
                     'class="hqgaw">МИД России</a></p>']
        replacement_result = self.html_text_parser.replace_html_tags(test_data)
        self.assertEqual(replacement_result, ['blablabla. [/tags/organizations/mid/]'])


    def test_paragraph_offsets(self):
        #test_data = ['<p>1</p>','<p>2</p>','<title>1</title>']
        #test_text = self.html_text_parser.generate_text_by_data(test_data)
        #self.assertEqual(test_text,"<p>1</p>\n<p>2</p>\n<title>1</title>")
        pass


if __name__ == '__main__':
    unittest.main()
