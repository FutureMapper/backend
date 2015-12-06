from django.conf.urls import *
from profiles.views import profile_list

USERNAME = r'(?P<username>[-.\w]+)'

urlpatterns = patterns('profiles.views',
    url(r'^edit/$',
        view='profile_edit',
        name='profile_edit',
    ),
    url(r'^%s/$' % USERNAME,
        view='profile_detail',
        name='profile_detail',
    ),
    url (r'^$',
        view=profile_list.as_view(),
        name='profile_list',
    ),
)