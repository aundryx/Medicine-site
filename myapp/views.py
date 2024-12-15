from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def ccold(request):
    return render(request, 'myapp/cold.html')

def cough(request):
    return render(request, 'myapp/cough.html')

def fever(request):
    return render(request, 'myapp/fever.html')

def highB(request):
    return render(request, 'myapp/hblood.html')

def headache(request):
    return render(request, 'myapp/headache.html')

def hloss(request):
    return render(request, 'myapp/hairloss.html')

def contact(request):
    return render(request, 'myapp/contacts.html')
