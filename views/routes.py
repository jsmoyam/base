from views.router import Router, DataStrategyEnum
from views.index_view import index_view
from views.profile_view import profile_view
from views.settings_view import settings_view
from views.data_view import data_view
from views.login_view import login_view
from views.register_view import register_view

router = Router(DataStrategyEnum.QUERY)

routes = {
    "/": {"label": "Home", "view": index_view},
    "/login": {"label": "Login", "view": login_view},
    "/register": {"label": "Register", "view": register_view},
    "/profile": {"label": "profile", "view": profile_view},
    "/settings": {"label": "Settings", "view": settings_view},
    "/data": {"label": "data", "view": data_view}
}

router.routes = routes


