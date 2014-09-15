from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.views.generic import View, FormView
from django.utils.decorators import method_decorator
from forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                '',
                ['fantasy090633@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site'})
    return render_to_response('contact_form.html', {'form': form, })


def interceptor_test(method):
    def new_method(request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST.get('subject', '') == 'xxx':
                raise Http404
        return method(request, *args, **kwargs)
    return new_method


class Contact(View):
    form_class = ContactForm
    template_name = 'contact_form.html'
    my_initial = {'subject': 'Class url'}

    def get(self, request):
        form = self.form_class(initial = self.my_initial)
        return render_to_response(self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                '',
                ['fantasy090633@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
        return render_to_response(self.template_name, {'form': form})

    @method_decorator(interceptor_test)
    def dispatch(self, *args, **kwargs):
        return super(Contact, self).dispatch(*args, **kwargs)


def contact_thanks(request):
    return HttpResponse('Thanks!')


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/contact/thanks/'

    def form_valid(self, form):
        print('xxx')
        return super(ContactView, self).form_valid(form)
