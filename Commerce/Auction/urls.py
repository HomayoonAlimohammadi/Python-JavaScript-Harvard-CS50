from django.urls import path
from .views import (
    index_view,
    listing_view,
    create_listing_view,
    edit_listing_view,
    delete_listing_view,
    close_listing_view,
    login_view,
    logout_view,
    register_view,
    search_view,
    toggle_watch,
    watchlist_view,
)


app_name = 'auction'
urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('listings/search/', search_view, name='search'),
    path('listings/create/', create_listing_view, name='create_listing'),
    path('listings/watchlist/', watchlist_view, name='watchlist'),
    path('listings/<int:id>/', listing_view, name='listing'),
    path('listings/<int:id>/edit/', edit_listing_view, name='edit_listing'),
    path('listings/<int:id>/delete/', delete_listing_view, name='delete_listing'),
    path('listings/<int:id>/close/', close_listing_view, name='close_listing'),
    path('listings/<int:id>/toggle-watch/', toggle_watch, name='toggle_watch'),
]