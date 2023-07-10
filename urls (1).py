#from django.urls import path
#from .views import WishlistView

#urlpatterns = [
    # Остальные URL-маршруты
    #path('wishlist/', WishlistView.as_view(), name='wishlist'),
#]

from django.urls import path
from .views import WishlistView, AddToWishlistView, RemoveFromWishlistView

urlpatterns = [
    # Остальные URL-маршруты
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('add_to_wishlist/', AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('remove_from_wishlist/', RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),
]
