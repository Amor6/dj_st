from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, index, collection, product_id

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('collection/', collection, name='collection'),
    path('<int:id>/prod/', product_id, name='product_pk'),
]
