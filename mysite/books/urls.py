from django.conf.urls import patterns, include, url

from books.models import Book, Author
from books.views import PublisherList,PublisherDetail


urlpatterns = patterns('books.views',
                        (r'^author_list/$', 'obj_list', {'model': Author}),
                        (r'^book_list/$', 'obj_list', {'model': Book}),
                        url(r'publishers/$', PublisherList.as_view()),
                        (r'^search/$', 'search'),
)