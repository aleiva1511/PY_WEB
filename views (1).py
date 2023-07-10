#from django.shortcuts import render, redirect
#from django.views import View
#from .models import Wishlist

#class WishlistView(View):
    #def get(self, request):
        #if request.user.is_authenticated:
            #wishlist = Wishlist.objects.get(user=request.user)
            #products = wishlist.products.all()
            #return render(request, "store/wishlist.html", {"products": products})
        #return redirect('login:login')

from django.shortcuts import render, redirect
from django.views import View
from .models import Wishlist, Product
from django.http import JsonResponse

class WishlistView(View):
    def get(self, request):
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.get(user=request.user)
            products = wishlist.products.all()
            return render(request, "store/wishlist.html", {"products": products})
        return redirect('login:login')

class AddToWishlistView(View):
    def post(self, request):
        if request.user.is_authenticated:
            product_id = request.POST.get("product_id")
            product = Product.objects.get(id=product_id)
            wishlist = Wishlist.objects.get(user=request.user)
            wishlist.products.add(product)
            return JsonResponse({"message": "Product added to wishlist."})
        return JsonResponse({"message": "User not authenticated."})

class RemoveFromWishlistView(View):
    def post(self, request):
        if request.user.is_authenticated:
            product_id = request.POST.get("product_id")
            product = Product.objects.get(id=product_id)
            wishlist = Wishlist.objects.get(user=request.user)
            wishlist.products.remove(product)
            return JsonResponse({"message": "Product removed from wishlist."})
        return JsonResponse({"message": "User not authenticated."})
