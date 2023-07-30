import re


class Sentence:
    def __init__(self, text) -> None:
        self.__text = text
        self.__e = self.__get_sentence()

    def __getitem__(self, idx):
        return self.__e[idx]

    def __get_sentence(self):
        pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
        return re.split(pattern, self.__text)
