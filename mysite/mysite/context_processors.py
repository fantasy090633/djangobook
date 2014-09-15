def customer_proc(request):
    return {'APP': 'My app in context_processors', 'USER': request.user, 'IP_ADDRESS': request.META['REMOTE_ADDR']}