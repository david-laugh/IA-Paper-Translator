from io import BytesIO

from paper_translator.usecase.get_paper_copus import execute as gpc

from pywebio import start_server
from pywebio.input import file_upload
from pywebio.output import put_file


def App():
    pdf = file_upload("Select a Paper(.pdf):", accept=".pdf")
    filename = pdf["filename"][:-4] + "_translated.txt"
    content = pdf["content"]
    translated = gpc(BytesIO(content))
    put_file(filename, translated.encode(), 'download me')


if __name__ == "__main__":
    start_server(
        App,
        port=2030,
        auto_open_webbrowser=True)
