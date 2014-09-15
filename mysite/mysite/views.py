import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.generic.base import View


def hello(request):
    return HttpResponse('Hello World')


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset='1'):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'next_time': dt, 'offset': offset})


def display_meta(request):
    return render_to_response('meta.html', {'meta': request.META.items()})


def foobar_view(request, template_name):
    return render_to_response(template_name, {'hello': 'Hello'})


def customer_proc(request):
    return {'APP': 'My app in view', 'USER': request.user, 'IP_ADDRESS': request.META['REMOTE_ADDR']}


def view_1(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am view 1.'}, processors=[customer_proc])
    return HttpResponse(t.render(c))


def view_2(request):
    return render_to_response('template1.html', {'message': 'I am view second.'},
                              context_instance=RequestContext(request, processors=[customer_proc]))


def view_3(request):
    return render_to_response('template1.html', {'message': 'I am view 3rd.'},
                              context_instance=RequestContext(request))


def html_escaping(request):
    return render_to_response('html_escaping.html', {'tag_h1': '<h1>Hello</h1>'})


class MyView(View):
    greeting = 'Hello'

    def get(self, request):
        return HttpResponse('get %s' % self.greeting)

    def post(self, request):
        return HttpResponse('post')


class MyViewEd(MyView):
    greeting = 'Hi'