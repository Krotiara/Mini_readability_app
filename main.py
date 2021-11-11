from App import TextWriter as TW
from App import WebPagesHandler as WH
from App import HTMLTextParser as HP


def generate_readability_text(url: str, text_width: int = 80):
    web_parser = WH.WebPagesParser()
    html_parser = HP.HTMLTextParser()
    text_writer = TW.TextWriter()
    text = html_parser.generate_readability_text(web_parser.get_html_data(url), text_width)
    text_writer.write_by_url_format(text, url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #https://www.codementor.io/@sheena/how-to-write-python-custom-exceptions-du107ufv9
    #https://www.programiz.com/python-programming/user-defined-exception
    #https://www.gazeta.ru/politics/2021/11/10_a_14189233.shtml - не заменилась одна <a> и нужно обработку картинок сделать
    # 'https://www.gazeta.ru/politics/2021/11/10_a_14189233.shtml' - не заменилась одна <a>
    # 'http://www.differencebetween.net/science/nature/differences-between-imitation-and-modeling/' - big ссылка
    # трэш с https://pythonworld.ru/osnovy/dekoratory.html
    # https://forums.playground.ru/forza_horizon_5/vpechatleniya_ot_igry-1007420/ - все в div - на будущее
    generate_readability_text('http://www.differencebetween.net/science/nature/differences-between-imitation-and-modeling/', 80)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
