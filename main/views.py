from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        "title": "Home - О нас", 
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)


def contact(request):
    context = {
        "title": "Contact - Главная",
        "content": "Как с нами можно связаться:",
        "phone": "067-127-57-67"
    }

    return render(request, 'main/contact.html', context) 


def delivery(request):
    context = {
        "title": "Delivery - Главная",
        "content": "Доставка и оплата",
    }

    return render(request, "main/delivery_pay.html", context)
