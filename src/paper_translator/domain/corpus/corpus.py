from pypdf import PdfReader


class Corpus:
    def __init__(self, pdf_path: str) -> None:
        self.__pdf_path = pdf_path
        self.text = self.__get_text()

    def __get_text(self):
        content = []
        reader = PdfReader(self.__pdf_path)
        for page in reader.pages:
            text = page.extract_text()
            text = text.replace("\n", " ").replace("- ", "")
            content.append(text)
        return " ".join(content)
