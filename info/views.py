from django.shortcuts import render
from django.http import HttpResponse

def main_page(request, name="Аліно", color=""):
    return render(request, 'info/main_page.html', {'name': name, 'color': color})

def couples(request):
    return render(request, 'info/couples.html')

def forum(request):
    return render(request, 'info/forum.html')

def apply(request):
     return render(request, 'info/apply.html')
