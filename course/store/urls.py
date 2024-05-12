from django.urls import path

from .views import item_details, store, price, contact

app_name = 'store'


urlpatterns = [
    path('', store, name='home'),
    path('price/', price, name='price'),
    path('contact/', contact, name='contact'),
    path('<slug:item_slug>/', item_details, name='item_details'),
]
