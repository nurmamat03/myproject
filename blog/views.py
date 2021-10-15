from django.shortcuts import render
from .models import News, Portfolio



def home(request):
    images = News.objects.all()
    img = Portfolio.objects.all()
    return render(request, 'index.html', {'images': images, 'img': img})

