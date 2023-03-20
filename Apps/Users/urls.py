from django.urls import path
from Apps.Users.views import home, sign_up


urlpatterns = [
    path('', home, name='home'),
    path('sign_up/', sign_up, name='sign_up'),
]
