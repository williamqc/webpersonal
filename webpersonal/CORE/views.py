from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")