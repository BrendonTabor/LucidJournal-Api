from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from LucidJournalapi.views import (
    register_user,
    login_user,
    get_current_user,
    Entryview,
    SleepFactorView,
    RemCountView,
    WakeMethodView
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"entries", Entryview, "entry")
router.register(r"sleepfactors", SleepFactorView, "sleepfactor")
router.register(r"remcount", RemCountView, "remcount")
router.register(r"wakemethod", WakeMethodView, "wakemethod")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("admin/", admin.site.urls),
    path("current_user", get_current_user),
]
