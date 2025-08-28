from django.urls import path
from django.contrib.auth import views as auth_views
from .views import main,index,Product_Detail_view,about,RegisterView,CustomLoginView,login,Product_category_view,checkoutform
from .forms import LoginForm
urlpatterns = [
    path('main/',main,name='main'),
    path('about/',about,name='about'),
    path('login/',CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                        authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/',RegisterView.as_view(),name='signup'),
    path('',index,name='index'),
    path('category/<slug:slug>/',Product_Detail_view,name='product-detail'),
    path('product/<slug:cat>/',Product_category_view,name='product-category'),
    path('checkoutform/',checkoutform,name='checkoutform'),
    ]


