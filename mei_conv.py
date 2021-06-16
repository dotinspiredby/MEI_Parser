import requests
from music21 import mei
import sys


class ParserConverter:

    def __init__(self, link):
        self.score = self.__parse_link(link)

    @staticmethod
    def __parse_link(url):
        parsed = requests.get(url)
        to_conv = mei.MeiToM21Converter(parsed.text)
        stream_obj = to_conv.run()
        return stream_obj

    def run(self):
        self.score.show()


if __name__ == "__main__":
    new = ParserConverter(sys.argv[1])
    new.run()
