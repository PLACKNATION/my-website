from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home/home_page.html', context)

def about_page(request):
    context = {}
    return render(request, 'home/base.html', context)

def contact_page(request):
    context = {}
    return render(request, 'home/base.html', context)