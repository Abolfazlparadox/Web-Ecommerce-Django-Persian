from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from .models import product,discount,category,CommentReply,OrderProduct,order,Comment
from django.http import Http404,JsonResponse
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib  import messages
from .forms import RegisterForm,LoginForm,CommentForm,CommentReplyForm



# Create your views here.

def main(request,*args, **kwargs):
    Category = category.objects.all()
    context = {
        'Category':Category
    }
    return render(request,"main.html",context)

# view all product function 
def index(request):

    discount_products = product.objects.filter(discount__status=True)
    prices = [product.price for product in discount_products]
    
    discount_price = [product.discount.value for product in discount_products]
    
    discounted_price = [price *  discount_value for price, discount_value in zip(prices, discount_price)]
    for Product, discounted_price in zip(discount_products, discounted_price):
        Product.discounted_prices = discounted_price
        Product.save()
    Category = category.objects.all()
    all_products = product.objects.all()
    
    context = { 
        'Category':Category,
        'product':all_products,
        'discounted_prices':discounted_price
    }
    return render(request, 'index.html', context)
def Product_Detail_view(request, slug=None, *args, **kwargs):
    Product = product.objects.get(slug=slug) # slug url
    all_products = product.objects.all()

    Category = category.objects.all()
    comments = Comment.objects.all().filter(product=Product)
    if Product is None:
        print("product Doesn't exist ")
        raise Http404("product Doesn't exist ")
    
    if request.method == 'POST':
        
        if 'reply_id' in request.POST: # if the submit button for replying to a comment is clicked
            comment_id = request.POST.get('reply_id')# get the comment id
            comment = Comment.objects.get(id=comment_id) # get the comment
            reply_form = CommentReplyForm(request.POST)
            # create the reply form with the request data
            if reply_form.is_valid():
                
                new_name = reply_form.cleaned_data['name_reply']
                new_email = reply_form.cleaned_data['email_reply']
                new_massage = reply_form.cleaned_data['massage_reply']
                new_reply = CommentReply(comment=comment, name=new_name, email=new_email, massage=new_massage)
                new_reply.save()
        else: # if the submit button for creating a new comment is clicked
            form = CommentForm(request.POST)
            if form.is_valid():
                
                new_name = form.cleaned_data['name']
                new_email = form.cleaned_data['email']
                new_massage = form.cleaned_data['massage']
                new_comment = Comment(product=Product, name=new_name, email=new_email, massage=new_massage)
                new_comment.save()

    context = {
        'object': Product,
        'product': all_products,
        'Category': Category,
        'comments': comments,
    }
    return render(request, "index_product.html", context)
def Product_category_view(request,cat=None,*args,**kwargs):
    cat =cat.replace('-'," ")

    Category1 = category.objects.all()
    try:
        Category = category.objects.get(name=cat) 
        product_category = product.objects.filter(category=Category)
        context = {
            'product':product_category,
            'Category':Category1,
            }
        return render(request,"index.html",context)
    except:
        messages.WARNING(request, f'This {Category} category are not exist ')
        return redirect("index")
def about(request):
    Category = category.objects.all()
    all_products = product.objects.all()
    context = { 
        'Category':Category,
        'product':all_products,
        }
    
    return render(request,"about.html",context)
def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
# login_form as Class View
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        Category = category.objects.all()
        return render(request, self.template_name, {'form': form,'Category':Category,})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        Category = category.objects.all()

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form,'Category':Category,})
# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        Category = category.objects.all()
        return render(request, self.template_name, {'form': form,'Category':Category,})
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def checkoutform(request,*args, **kwargs):
    return render(request,"checkout-rtl-form.html",{})