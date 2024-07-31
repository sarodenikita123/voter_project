from django.urls import path
from .views import *


urlpatterns = [
    path("create/", create_view, name='create_url'),
    path("show/", show_view, name='show_url'),
    path("details/<int:pk>/", details, name='details_url'),
    path("update/<int:pk>/", update_view, name='update_url'),
    path("delete/<int:pk>/", delete_view, name='cancel_url'),
]
handler404 = 'crud_app.views.handler404'
