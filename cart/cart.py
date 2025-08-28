from Shop.models import product
class Cart():
    def __init__(self,request):
        self.session = request.session

        cart=self.session.get('session_key')
        if 'session_key' not in request.session:
            cart =self.session['session_key']={}

        self.cart = cart
    def add(self,product,quantity):
        product_id=str(product.id)
        product_qty=str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
    def __len__(self):
        
        return len(self.cart)
    def get_product(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use ids to lookup products in database model
        products= product.objects.filter(id__in=product_ids)
        #return those products 
        return products
    def get_quants(self):
        quantities = self.cart
        return quantities
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        our_cart = self.cart
        our_cart[product_id] = product_qty
        self.session.modified = True
        thing = self.cart
        return thing
    def delete(self,product):
        product_id = str(product)
        our_cart= self.cart
        if product_id in our_cart:
            del our_cart[product_id];
        self.session.modified = True
    def cart_total(self):
        product_ids = self.cart.keys()
        products = product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total= 0
        for key , value in quantities.items():
            
            key = int(key)
            for Product in products:
                if Product.id == key:
                    if Product.discounted_prices != 0 :
                            total = total+(Product.discounted_prices*value)
                    else:
                        total = total+(Product.price*value)
        return total       