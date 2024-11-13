from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories

class IndexView(TemplateView):
    template_name= "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = "Магазин мебели Home"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - О нас"
        context["content"] = "О нас"
        context["text_on_page"] = "Текст о том почему этот магазин такой классный, и какой хороший товар."
        return context

class ContactView(TemplateView):
    template_name = "main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact - Главная"
        context["content"] = "Как с нами можно связаться:"
        context["phone"] = "067-127-57-67"
        return context

class DeliveryView(TemplateView):
    template_name= "main/delivery_pay.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delivery - Главная"
        context["content"] = "Доставка и оплата"
        return context


# def index(request):
#     context = {
#         "title": "Home - Главная",
#         "content": "Магазин мебели Home",
#     }

#     return render(request, "main/index.html", context)


# def about(request):
#     context = {
#         "title": "Home - О нас",
#         "content": "О нас",
#         "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар."
#     }

#     return render(request, 'main/about.html', context)


# def contact(request):
#     context = {
#         "title": "Contact - Главная",
#         "content": "Как с нами можно связаться:",
#         "phone": "067-127-57-67"
#     }

#     return render(request, 'main/contact.html', context)


# def delivery(request):
#     context = {
#         "title": "Delivery - Главная",
#         "content": "Доставка и оплата",
#     }

#     return render(request, "main/delivery_pay.html", context)
