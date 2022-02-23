from django.urls import path
from . import views
from django.conf.urls.static import static
from django_store import settings

urlpatterns = [
    path('', views.index, name='store.home'),
    path('product/<int:pid>', views.product, name='store.product'),
    path('category/<int:cid>', views.category, name='store.category'),
    path('category', views.category, name='store.category'),
    path('cart', views.cart, name='store.cart'),
    path('cart/add/<int:pid>', views.cart_update, name='store.cart_add'),
    path('cart/remove/<int:pid>', views.cart_remove, name='store.cart_remove'),
    path('cart', views.cart, name='store.cart'),
    path('checkout', views.checkout, name='store.checkout'),
    path('checkout/complete', views.checkout_complete, name='store.checkout_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

