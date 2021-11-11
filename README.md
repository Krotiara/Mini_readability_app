# Mini_readability_app
Загрузчик полезной информации с веб-страницы. По входной url ссылке на статью выгружает и обрабатывает с веб-страницы
поля, указанные в настройках.

Руководство запуска:
Ключи:
-h - help.
-url - указание url адреса ресурса, откуда необходимо загрузить текст.
-w - указание ограничивающей ширины текса.
-s - Название файла настроек выгрузки. (с расширением)

Настройка выгрузки:
Настройки выгрузки располагаются в папке Settings и представляют собой текстовые файлы с указанием следующих пар
ключ-значение:
1) text_width - ограничивающая ширина текста (целое число через =)
2) searching_tags - тэги, которые необходимо выгрузить с веб-страницы. 
   Указываются через = через запятую. Например, searching_tags=p,h,title,span.
   Приоритет у ключа -w больше, чем у записи параметра ширины в файле настроек.

Для запуска программы необходимо в командной строке написать следующее:
python main.py -url url_address и опционально указать ключи -w и -s. Если не указывать, будут использоваться значения
по-умолчанию: ширина текста=80, тэги=p,title,h,span,img.

Результат работы программы - созданный текстовый файл, который автоматически помещается в папку согласно url-шаблону:
http://lenta.ru/news/2013/03/dtp/index.html => [Texts]/lenta.ru/news/2013/03/dtp/index.txt

Направления улучшения/развития программы:
1) Замена переноса строк по словам на перенос с разбиением слова с целью полноценного выравнивания по ширине строки.
2) Добавление различных настроек для загрузки разнообразной полезной информации с веб-страницы. Как, например,
выгрузка ссылок на картинки, которая задается файлом настроек images_set.txt.
3) При необходимости можно добавить парсер XML (например) файлов. Тогда имеет смысл сделать абстрактный класс парсера с
переопределяемыми методами generate_readability_text и т.д.
4) Добавление обработки div блоков html.
Например, весь текст https://www.researchgate.net/blog/post/springer-nature-and-researchgate-to-move-forward-with-long-
term-content-sharing-partnership содержится в div блоках.

   
Тестируемые URL:
https://www.codementor.io/@sheena/how-to-write-python-custom-exceptions-du107ufv9
https://www.programiz.com/python-programming/user-defined-exception
https://www.gazeta.ru/politics/2021/11/10_a_14189233.shtml
http://www.differencebetween.net/science/nature/differences-between-imitation-and-modeling/

P.S. Парсинг html сделан без Beautiful Soup в силу ограничения в тз: "Не должно использоваться
сторонних библиотек, впрямую решающих задачу."