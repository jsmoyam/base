# Sidebar class
from functools import partial

from flet_core import UserControl, Row, Container, Text, ButtonStyle, RoundedRectangleBorder, MainAxisAlignment, \
    padding, alignment, Column, Divider, icons, IconButton


class ModernNavBar(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()

    def HighLight(self, e):
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()
            e.control.content.controls[0].icon_color = 'white'
            e.control.content.controls[1].color = 'white'
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = 'white54'
            e.control.content.controls[1].color = 'white54'
            e.control.content.update()

    def UserData(self, initials: str, name: str, description: str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=42,
                        content=Text(
                            value=initials,
                            size=20,
                            weight='bold'
                        ),
                    ),
                    Column(
                        spacing=1,
                        alignment='center',
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200,
                            ),
                            Text(
                                value=description,
                                size=9,
                                weight='w400',
                                color='white54',
                                opacity=1,
                                animate_opacity=200,
                            ),
                        ]
                    )
                ]
            )
        )

    def containedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                '': RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={'': 'transparent'},
                        ),
                    ),
                    Text(
                        value=text,
                        color='white54',
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            )
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment='center',
                controls=[
                    self.UserData("JS", "Juan Salvador", "Engineer"),

                    # clickable to minimize/expand

                    #Container(
                    #    width=24,
                    #    height=24,
                    #    bgcolor='bluey',
                    #    border_radius=8,
                    #    on_click=partial(self.func),
                    #),

                    Divider(height=5, color='transparent'),
                    self.containedIcon(icons.SEARCH, 'Search'),
                    self.containedIcon(icons.DASHBOARD_ROUNDED, 'Dashboard'),
                    self.containedIcon(icons.BAR_CHART, 'Revenue'),
                    self.containedIcon(icons.NOTIFICATIONS, 'Notifications'),
                    self.containedIcon(icons.PIE_CHART_ROUNDED, 'Analytics'),
                    self.containedIcon(icons.FAVORITE_ROUNDED, 'Likes'),
                    self.containedIcon(icons.WALLET_ROUNDED, 'Wallet'),
                    Divider(height=5, color='white24'),
                    self.containedIcon(icons.LOGOUT_ROUNDED, 'Logout'),
                ]
            ))
