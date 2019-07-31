from django.shortcuts import render
from .models import Prices, About, Frontpage


ABOUT_PAGE = About.objects.all()
PRICES_PAGE = Prices.objects.all()
FRONT_PAGE = Frontpage.objects.filter()[:1].get()

def index(request):
    """ Home """
    return render(request, 'psychotherapy/index.html', {"front_page": FRONT_PAGE})

def therapy(request):
    """ Shows information regarding this specific sort of therapy."""
    return render(request, 'psychotherapy/pages/therapy.html')

def getstarted(request):
    """ Shows contact information and a form to contact."""
    return render(request, 'psychotherapy/pages/contact.html')

def about(request):
    """ Shows information about the company."""
    return render(request, 'psychotherapy/pages/about.html')
    
def prices(request):
    """ Shows a price list of different sorts of therapy."""
    return render(request, 'psychotherapy/pages/prices.html')