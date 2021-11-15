class TextWidthException(Exception):
    def __init__(self, width, word_width, word):
        self.width = width
        self.message = 'Impossible text width, words length in input text' \
                       ' is more than width parameter:\nwidth = {}\n'\
                       'word width = {}\nword = {}'\
            .format(width,word_width,word)
        super().__init__(self.message)