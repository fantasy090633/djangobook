from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from books.models import Book, Publisher


def search_from(request):
    return render_to_response('search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})


def obj_list(request, model):
    obj_list = model.objects.all()
    template_name = '%s_list.html' % model.__name__.lower()
    return render_to_response(template_name, {'obj_list': obj_list})


class PublisherList(ListView):
    model = Publisher
    template_name = 'books/publisher_list.html'
    # same with model = Publisher, but we can use this filter or order data
    # queryset = Publisher.objects.all()
    # queryset = Publisher.objects.order_by('-publication_date')
    # queryset = Book.objects.filter(publisher__name='Acme Publishing')
    context_object_name = 'publishers_list'


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context