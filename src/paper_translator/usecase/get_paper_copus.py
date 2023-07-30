from easynmt import EasyNMT

from paper_translator.domain import Corpus, Sentence


def execute(pdf_path):
    model = EasyNMT('m2m_100_418M')

    pdf_corpus = Corpus(pdf_path)
    sentences = Sentence(pdf_corpus.text)
    translated = ""
    for sentence in sentences[:]:
        try:
            translated_sentence = model.translate(sentence, target_lang='ko', source_lang='en')
            translated += f"{sentence}\n{translated_sentence}\n"
        except Exception as e:
            print(f"{e}")
    return translated


if __name__ == "__main__":
    pdf_path = "example/1812.00285.pdf"
    execute(pdf_path)
