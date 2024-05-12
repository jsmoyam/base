from flet import TextField, TextAlign
from flet_core import ElevatedButton, ControlEvent, Row, Column, MainAxisAlignment


def login_view(router):
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        e.page.update()

    def submit(e: ControlEvent) -> None:
        if text_username.value == 'j' and text_password.value == '1':
            e.page.go('/')

    def register(e: ControlEvent) -> None:
        e.page.go('/register')

    text_username: TextField = TextField(label='Username', text_align=TextAlign.LEFT, width=200, on_change=validate)
    text_password: TextField = TextField(label='Password', text_align=TextAlign.LEFT, width=200, on_change=validate,
                                         password=True)
    button_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True, on_click=submit)
    button_register: ElevatedButton = ElevatedButton(text='Register', width=200, on_click=register)

    content = Row(
        controls=[
            Column([text_username, text_password, button_submit, button_register])
        ],
        alignment=MainAxisAlignment.CENTER
    )

    return content
