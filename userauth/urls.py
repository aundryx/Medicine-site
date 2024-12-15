from django.urls import re_path
import userauth.views

urlpatterns = [
    re_path(r'^$', userauth.views.login_user, name='login'),
    re_path(r'^login/$', userauth.views.login_user, name='login'),
    re_path(r'^register/$', userauth.views.register_user, name='register'),

]