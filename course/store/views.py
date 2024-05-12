from django.shortcuts import get_object_or_404, render

from .models import Item
from .paginator import paginator


def store(request):
    items = Item.objects.filter(is_available=True)
    context = {
        'page_obj': paginator(request, items, 6),
        'range': [*range(1, 7)],
    }

    return render(request, 'store/main_page.html', context)


def item_details(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'store/item_details.html', context)

def price(request):
    items = Item.objects.filter(is_available=True)
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],
    }

    return render(request, 'store/price.html', context)

def contact(request):

    return render(request, 'store/contact.html')
