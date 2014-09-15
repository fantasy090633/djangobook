from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import MyViewEd

admin.autodiscover()

urlpatterns = patterns('mysite.views',
                       (r'^hello/$', 'hello'),
                       (r'^time/$', 'current_datetime'),
                       (r'^meta/$', 'display_meta'),
                       (r'^time/plus/$', 'hours_ahead'),
                       (r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),
                       (r'^hello1/$', 'foobar_view', {'template_name': 'hello1.html'}),
                       (r'^hello2/$', 'foobar_view', {'template_name': 'hello2.html'}),
                       (r'^view1/$', 'view_1'),
                       (r'^view2/$', 'view_2'),
                       (r'^view3/$', 'view_3'),
                       (r'^html_escaping/$', 'html_escaping'),
                       (r'^about/$', MyViewEd.as_view()),
                       (r'^about2/$', MyViewEd.as_view(greeting='World')),
                       (r'^$', 'hello'),
)

urlpatterns += patterns('',
                        # Examples:
                        # url(r'^$', 'mysite.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^book/', include('books.urls')),
                        url(r'^contact/', include('contact.urls')),
)