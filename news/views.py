from django.shortcuts import render
from .models import News

def news(request):
    noticias = News.objects.all().order_by('-date')
    return render(request, 'news.html',{'noticias':noticias})
