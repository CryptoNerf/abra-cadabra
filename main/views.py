from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def buypage(request):
    context = {
        'title': 'Украшения Мари',
        'content': "Магазин Украшений"
    }


    return render(request, 'main/buypage.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': "О нас",
        'textonpage': "Жопа слона зуба орла череп коня летучий голандец бобра",

    }

    return render(request, 'main/about.html', context)
