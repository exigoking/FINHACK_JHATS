from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'FINHack_mainapp.views.home', name='home'),
    url(r'^createroom/', 'FINHack_mainapp.views.create_room', name='createroom'),
    url(r'^invite/', 'FINHack_mainapp.views.invite', name='invite'),
    url(r'^api/', 'FINHack_mainapp.views.get_info', name='get_info'),

    url(r'^admin/', include(admin.site.urls)),
]
