from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    context = {}
    return render(request, "home/base.html", context)

def about_page(requests):
    return HttpResponse("<h1> About Page </h1>")

def contact_page(requests):
    return HttpResponse("<h1> Contact Page </h1>")