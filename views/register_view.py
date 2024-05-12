from flet import TextField, TextAlign
from flet_core import ElevatedButton, ControlEvent, Row, Column, MainAxisAlignment, KeyboardType, Checkbox
from supabase import create_client, Client

url: str = "http://192.168.1.42:8000"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICJyb2xlIjogImFub24iLAogICJpc3MiOiAic3VwYWJhc2UiLAogICJpYXQiOiAxNzExMjM0ODAwLAogICJleHAiOiAxODY5MDAxMjAwCn0.7mhHxtCER_Fw_BoyPGzD1yCc2I1e_M16r5SoSvjL1Wk"
supabase: Client = create_client(url, key)

def register_view(router):
    def validate(e: ControlEvent) -> None:
        button_submit.disabled = True
        if all([text_name.value, text_email.value, text_password.value, text_password_again.value]):
            if text_password.value != text_password_again.value:
                return
            if checkbox_company.value:
                if all([text_company_name.value]):
                    button_submit.disabled = False
            else:
                button_submit.disabled = False
        e.page.update()

    def swap_company_data(e: ControlEvent) -> None:
        text_company_name.visible = not text_company_name.visible
        e.page.update()

    def submit(e: ControlEvent) -> None:
        res = supabase.auth.sign_up({
            "email": text_email.value,
            "password": text_password.value,
            "options": {
                "data": {
                    "name": text_name.value,
                    "company": checkbox_company.value,
                    "company_name": text_company_name.value,
                }
            }
        })

    text_name: TextField = TextField(label='Name', text_align=TextAlign.LEFT, width=200, on_change=validate)
    text_email: TextField = TextField(label='Email', text_align=TextAlign.LEFT, width=200,
                                      keyboard_type=KeyboardType.EMAIL)
    text_password: TextField = TextField(label='Password', text_align=TextAlign.LEFT, width=200, password=True,
                                         can_reveal_password=True)
    text_password_again: TextField = TextField(label='Repeat password', text_align=TextAlign.LEFT, width=200,
                                               on_change=validate, password=True, can_reveal_password=True)
    checkbox_company: Checkbox = Checkbox(label='Register as company', value=False, on_change=swap_company_data)
    text_company_name: TextField = TextField(label='Company name', text_align=TextAlign.LEFT, width=200, visible=False,
                                             on_change=validate)
    button_submit: ElevatedButton = ElevatedButton(text='Register', width=200, disabled=True, on_click=submit)

    content = Row(
        controls=[
            Column([text_name, text_email, text_password, text_password_again, checkbox_company, text_company_name,
                    button_submit])
        ],
        alignment=MainAxisAlignment.CENTER
    )

    return content
