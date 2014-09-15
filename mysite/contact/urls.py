from django.conf.urls import patterns, include, url
from django.http import Http404
from views import contact, Contact


def interceptor_test(method):
    def new_method(request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST.get('subject', '') == 'xxx':
                raise Http404
        return method(request, *args, **kwargs)
    return new_method


urlpatterns = patterns('contact.views',
                        (r'^$', interceptor_test(contact)),
                        # Also use @method_decorator in contact/urls.py
                        # (r'^class/$', interceptor_test(Contact.as_view(my_initial={'subject': 'Class url in url.py'}))),
                        (r'^class/$', Contact.as_view(my_initial={'subject': 'Class url in url.py'})),
                        (r'^thanks/$', 'contact_thanks'),
)