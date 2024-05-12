import time

import flet
from flet_core import Page, Container, animation, alignment, Text, Column, colors, Row

from components.modernnavbar import ModernNavBar


def main(page: Page):
    # title
    page.title = 'Flet modern sidebar'

    # alignments
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def AnimateSidebar(e):
        if page.controls[0].width != 62:
            # reduce opacity of title text
            for item in (
                    # class
                    page.controls[0]
                            # content of the container
                            .content.controls[0]
                            # row controls
                            .content.controls[0]
                            # another layer
                            .content.controls[1]
                            # position of the text
                            .controls[:]
            ):
                item.opacity = (0)
                item.update()

            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()

            time.sleep(0.2)
            page.controls[0].width = 62
            page.controls[0].update()
        else:
            page.controls[0].width = 200
            page.controls[0].update()
            time.sleep(0.2)

            for item in (
                    # class
                    page.controls[0]
                            # content of the container
                            .content.controls[0]
                            # row controls
                            .content.controls[0]
                            # another layer
                            .content.controls[1]
                            # position of the text
                            .controls[:]
            ):
                item.opacity = 1
                item.update()

            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 1
                    items.content.update()


    # add class to page
    page.add(
        Row(
            controls=[
                Container(
                    width=200,
                    height=780,
                    bgcolor=colors.BLACK,
                    border_radius=10,
                    animate=animation.Animation(500, 'decelerate'),
                    alignment=alignment.top_center,
                    padding=10,
                    content=ModernNavBar(AnimateSidebar),
                ),
                Container(
                    width=700,
                    height=580,
                    bgcolor=colors.AMBER,
                    border_radius=10,
                    # animate=animation.Animation(500, 'decelerate'),
                    alignment=alignment.center,
                    padding=10,
                    content=Text(
                        value='HOLA'
                    )
                ),
            ]
        ),
        Column(
            controls=[

            ]
        )


    )

    page.update()

if __name__ == '__main__':
    flet.app(target=main)