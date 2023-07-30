import time

import googletrans
from easynmt import EasyNMT

from pywebio.output import put_progressbar, set_progressbar
from paper_translator.domain import Corpus, Sentence


def execute(pdf_path, language, mode):
    if mode == "fast":
        model = googletrans.Translator()
    else:
        model = EasyNMT('m2m_100_418M')

    if language == "chinese":
        target_lang = 'zh-cn'
        if mode == "elaborate":
            target_lang = 'zh'
    else:
        target_lang = 'ko'

    pdf_corpus = Corpus(pdf_path)
    sentences = Sentence(pdf_corpus.text)
    translated = ""

    put_progressbar('bar');
    for i, sentence in enumerate(sentences[:]):
        try:
            if mode == "elaborate":
                translated_sentence = model.translate(
                    sentence, target_lang=target_lang, source_lang='en')
            else:
                translated_sentence = model.translate(
                    sentence, dest=target_lang, src='en')
                time.sleep(1)
            translated += f"{sentence}\n{translated_sentence}\n"
        except Exception as e:
            print(f"{e}")
        set_progressbar('bar', i / len(sentences[:]))
    return translated


if __name__ == "__main__":
    pdf_path = "example/1812.00285.pdf"
    execute(pdf_path, 'korean', 'fast')
