from django.shortcuts import render
from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from django.http import Http404,JsonResponse
from Shop.models import product
from .cart import Cart


# Create your views here.

#CART Views
def cart_view(request):
    cart = Cart(request)
    cart_products= cart.get_product
    quantities = cart.get_quants
    totals=cart.cart_total()
    return render(request,"cart_view.html",{"cart_products":cart_products , "quantities":quantities , "total":totals})


def cart_add(request):
    # get the cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') =='post' :
        # get stuff 
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #lookup product in DB
        Product = get_object_or_404(product, id=product_id)
        #save to session
        cart.add(product=Product , quantity=product_qty)
        # get cart quantity
        cart_quantity = cart.__len__()
        #Return response
        response = JsonResponse({'qty' : cart_quantity})
        return response
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') =='post' :
        # get stuff 
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'products_id':product_id })
        return response
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') =='post' :
        # get stuff 
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        return response
