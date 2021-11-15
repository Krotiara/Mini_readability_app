import unittest
from App import WebPagesHandler as WPH
from App import HTMLTextParser as HTP
from App import CustomExceptions as CE
from App import TextGenerator


class Test(unittest.TestCase):
    def setUp(self):
        self.web_pages_handler = WPH.WebPagesParser()
        self.html_text_parser = HTP.HTMLTextParser()
        self.test_str = '<p>P tag without class</p>\nsimple text\n' \
                        '<p class="class1">P tag with class</p>\n' \
                        '<title>TITLE</title>\n<p class="hqeiq">blablabla. ' \
                        '<a href="/tags/organizations/mid/" ' \ 
                        'target="_blank" class="hqgaw">МИД России</a></p>'

    def test_regex_for_p_and_title_tags(self):
        parse_result = self.web_pages_handler.grap_needed_html_data(self.test_str)
        self.assertEqual(parse_result, ['<p>P tag without class</p>',
                                        '<p class="class1">P tag with class</p>',
                                        '<title>TITLE</title>',
                                        '<p class="hqeiq">blablabla.'
                                        ' <a href="/tags/organizations/mid/" ' \
                                        'target="_blank" class='
                                        '"hqgaw">МИД России</a></p>'])

    def text_regex_for_h_tags(self):
        test_text = '<h1 class="g">testclass</h1>blablabla<h2>test</h2>'
        parse_result = self.web_pages_handler.grap_needed_html_data(test_text)
        self.assertEqual(parse_result, ['<h1 class="g">testclass</h1>',
                                        '<h2>test</h2>'])

    def test_links_tags_replacement(self):
        raw_text = '<p class="hqeiq">blablabla. <a href="/tags/organizations' \
                   '/mid/" target="_blank" class="hqgaw">МИД ' \
                   'России</a></p>'
        text = self.html_text_parser.replace_link_tags(raw_text)
        self.assertEqual(text, '<p class="hqeiq">blablabla.'
                               ' [/tags/organizations/mid/]</p>')

    def test_paragraphs_offsets(self):
        test_data = 'blabla blabl ablablabla blabla blablablab labla' \
                    ' blablablabla\n' \
                    'blablablab lablab lablablabl ablablablabl ablablablabla' \
                    'bla blablablablablablablablab lablablablablab' \
                    'lablablablablab lablablablab lablablablabla\nblablablab' \
                    ' lablablablablablabl ablabla blablablablabla' \
                    'blablablab lablablablablablabla\nblablablabl ablablabla' \
                    ' blablablab lablablabl ablablablablablabla' \
                    'blabl ablablab lablabla blablablablablablablablabl' \
                    ' abl ablablablablablabl ablablabla blablablabla' \
                    'bla bla blablablablablablabl ablablabl ablablabla' \
                    ' blablabl abla\nbla'
        test_widths = [30, 40, 50, 80]
        for test_width in test_widths:
            test_data = self.html_text_parser.adjust_text_by_width(test_data,
                                                                   test_width)
            for line in test_data.split('\n'):
                self.assertTrue(len(line) <= test_width)

    def test_paragraphs_offsets_real_data(self):
        test_widths = [50, 80]
        for test_width in test_widths:
            text = TextGenerator.TextGenerator.generate_readability_text(
                'http://www.differencebetween.net/science/nature'
                '/differences-between-imitation-and-modeling/', test_width)
            for line in text.split('\n'):
                self.assertTrue(len(line) <= test_width)



if __name__ == '__main__':
    unittest.main()
