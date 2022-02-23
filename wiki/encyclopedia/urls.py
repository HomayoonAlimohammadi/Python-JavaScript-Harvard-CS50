from django.urls import path

from .views import (
    index,
    entry_view,
)

app_name = 'encyclopedia'
urlpatterns = [
    path("", index, name="index"),
    path('wiki/<str:title>/', entry_view, name='entry')
]
