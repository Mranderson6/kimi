from django.shortcuts import render

from blog.models import BlogPost, clientMessage, newsletter


# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        newsletter.objects.create(mail=email)
    return render(request, 'services/index.html', locals())


def contact(request):
    if request.method == 'POST':
        objet = request.POST.get('objet')
        nom = request.POST.get('nom')
        message = request.POST.get('message')
        mail = request.POST.get('email')
        clientMessage.objects.create(objet=objet, nom=nom, message=message, mail=mail)
    return render(request, 'services/contact.html')

def faq(request):
    return render(request, 'services/faq.html')

def about(request):
    articles = BlogPost.objects.all()
    return render(request, 'services/about.html', locals())

def error_404(request, exception):
    return render(request, '404.html')

def nosServices(request):
    return render(request, 'services/services.html')

