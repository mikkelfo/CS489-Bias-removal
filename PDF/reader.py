import tika
tika.initVM()
from tika import parser


class PDFReader:
    def __init__(self, file):
        self.parsed = parser.from_file(file, xmlContent=True)

    def title(self):
        return self.parsed['metadata']['title']

    def content(self):
        return self.parsed['content']


reader = PDFReader('../test/bias.pdf')
title = reader.title()
content = reader.content()
print(title)
