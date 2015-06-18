from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    url(r'^show/$', 'app.views.show', name='home'),
    url(r'^form/$', 'app.views.form', name='home'),
    url(r'^delete/(?P<id>\d+)/$', 'app.views.delete_new', name='home'),
    url(r'^details_form/$', 'app.views.details_form', name='home'),
    url(r'^train_list/$', 'app.views.train_list', name='home'),
    url(r'^login/$', 'app.views.Login', name='home'),
    url(r'^logout/$', 'app.views.logout_view', name='home'),
    url(r'^user_show/$', 'app.views.user_details', name='home'),
     url(r'^session/$', 'app.views.test_count_session', name='home'),
     url(r'^show_train/$', 'app.views.show_train_list', name='home'),
    url(r'^form_edit/(?P<id>\d+)/$', 'app.views.form_edit', name='home'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
