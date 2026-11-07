from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def dining(request):
    return render(request, 'dining.html')

def contact(request):
    return render(request, 'contact.html')

def offers(request):
    return render(request, 'offers.html')

def rooms(request):
    return render(request, 'rooms.html')

def room_detail(request, template_name):
    return render(request, template_name)

def offer_detail(request, template_name):
    return render(request, template_name)