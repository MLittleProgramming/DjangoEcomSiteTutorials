from django.urls import path
from . import views

app_name = 'ecomSiteApp'
urlpatterns = [
    path('createuser', views.create_user, name="createuser"),
    path('signup', views.signup, name="signup"),
]
