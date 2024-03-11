from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'services/index.html')


def contact(request):
    return render(request, 'services/contact.html')

def faq(request):
    return render(request, 'services/faq.html')

def about(request):
    return render(request, 'services/about.html')

def error_404(request, exception):
    return render(request, '404.html')

def nosServices(request):
    return render(request, 'services/services.html')

def blog(request):
    return render(request, 'services/blog.html')

def blogDetails(request, id):
    return render(request, 'services/blogDetails.html',locals())