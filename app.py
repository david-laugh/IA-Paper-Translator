from io import BytesIO
import os, signal

from paper_translator.usecase.get_paper_copus import execute as gpc

from pywebio import start_server
from pywebio.input import input_group, file_upload, select
from pywebio.output import popup, put_html, put_file, put_buttons, put_text
from pywebio.session import hold, set_env, eval_js


def restart():
    eval_js("window.open('http://localhost:2030/', '_blank')")
    eval_js("window.close()")


def end():
    eval_js("window.close()")
    os.kill(os.getpid(), signal.SIGTERM)


def App():
    set_env(title="Paper Translator")

    try:
        options = input_group("Options", [
            file_upload("Select a Paper(.pdf):", accept=".pdf", name='paper'),
            select('language', ['chinese', 'korean'], name='language'),
            select('mode', ['elaborate', 'fast'], name='mode'),
        ])

        filename = options["paper"]["filename"][:-4] + "_translated.txt"
        content = options["paper"]["content"]
        translated = gpc(BytesIO(content), options["language"], options["mode"])

        put_file(filename, translated.encode(), 'download me')

        put_text("", scope='ROOT')
        put_buttons(
            [dict(
                label="재시작",
                value='restart',
                color='success'
            ), 
            dict(
                label="종료",
                value='end',
                color='success'
            )],
            onclick=[restart, end],
            outline=True, scope='ROOT')

        hold()

    except Exception as e:
        popup(f'{e}', [
            put_html('<h3>프로그램을 종료합니다.</h3>'),
        ])


if __name__ == "__main__":
    start_server(
        App,
        port=2030,
        auto_open_webbrowser=True)
