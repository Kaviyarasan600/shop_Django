from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage, name="home"),
    path('about/', views.aboutPage, name="about"),
    path('category/', views.categoryPage, name="category"),
    path('category/<str:name>', views.subCategoryPage, name="category"),
    path('category/<str:cname>/<str:name>', views.productPage, name="products"),
    path('category/<str:cname>/<str:pname>/<str:name>', views.singleProductPage, name="single_product"),
    path('register/', views.registerPage, name="registerpage"),
    path('login/', views.loginPage, name="loginpage"),
    path('logout/',views.logoutRequest, name='logout'),
    path('cart/',views.cartPage, name='cartpage'),
    path('addtocart', views.add_to_cart, name= 'addtocart'),
    path('addtfav', views.addfav, name= 'addtfav'),
    path('removecart/<str:cid>', views.remove_cart, name='removecart'),
    path('favorites/',views.FavPage,name='favorites'),
    path('removefavorites/<str:fid>',views.remove_fav,name='removefavorites'),
    # path('updatecart', views.updateCart, name='updatecart'),
]
