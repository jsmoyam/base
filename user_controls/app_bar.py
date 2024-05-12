import flet as ft
# import views.routes
from views.routes import routes


def NavBar(page):
    def change_nav(e):
        nav_list = list(filter(lambda x: isinstance(x, ft.NavigationDrawerDestination), e.control.controls))
        selected_route = nav_list[e.control.selected_index]

        for route in routes:
            view = routes[route]
            if view["label"] == selected_route.label:
                page.go(route)
                page.drawer.open = False
                page.drawer.update()
                break

    page.drawer = ft.NavigationDrawer(
        selected_index=0,
        on_change=change_nav,
        controls=[
            ft.Container(height=15),
            ft.NavigationDrawerDestination(
                label='Home',
                icon=ft.icons.HOME,
                selected_icon_content=ft.Icon(ft.icons.HOME_FILLED),

            ),
            #ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label='Login',
                icon=ft.icons.LAPTOP_MAC,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),

            ),
            ft.NavigationDrawerDestination(
                label='Settings',
                icon=ft.icons.SETTINGS,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),

            ),
        ]
    )

    def open_menu(e):
        page.drawer.open = True
        page.drawer.update()

    NavBar = ft.AppBar(
        leading=ft.IconButton(
            icon=ft.icons.MENU,
            on_click=open_menu,
        ),
        leading_width=40,
        title=ft.Text("Flet Router"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
            ft.IconButton(ft.icons.PERSON_ROUNDED, on_click=lambda _: page.go('/profile')),
            ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings'))
        ]
    )

    return NavBar
