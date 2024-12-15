from django.urls import re_path
import myapp.views

urlpatterns = [
    re_path(r'^home$', myapp.views.home, name='home'),
    re_path(r'^about$', myapp.views.about, name='about'),
    re_path(r'^fever$', myapp.views.fever, name='fever'),
    re_path(r'^cough$', myapp.views.cough, name='cough'),
    re_path(r'^headache$', myapp.views.headache, name='headache'),
    re_path(r'^cold$', myapp.views.ccold, name='cold'),
    re_path(r'^hairloss$', myapp.views.hloss, name='hairloss'),
    re_path(r'^highblood$', myapp.views.highB, name='highblood'),
    re_path(r'^contact-us$', myapp.views.contact, name='contact'),
]