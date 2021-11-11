class TextWidthException(Exception):
    def __init__(self, width):
        self.width = width
        self.message = 'Impossible text width, words length in input text is more than width parameter = {}'\
            .format(width)
        super().__init__(self.message)