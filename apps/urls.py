from django.urls import path
from apps.views import index, homepagefunc, signupfunc, loginfunc

urlpatterns = [
    path('', homepagefunc, name='home'),
    path('register/', signupfunc, name='register'),
    path('login/', loginfunc, name='login'),
    path('my-profile/', index, name='my-profile'),
]