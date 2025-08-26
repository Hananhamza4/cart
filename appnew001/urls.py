from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('newfunc01',views.newfunc01,name="newfunc01"),
    # path('login',views.loginfun,name="loginfun"),
    path('',views.indexfun,name='indexfun'),
    path('404',views.error,name='error'),
    path('about',views.about,name='about'),
    # path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('news',views.news,name='news'),
    path('shop',views.shop,name='shop'),
    # path('signup',views.signup,name='signup'),
    path('singlen',views.singlen,name='singlen'),
    path('singlep/<int:id>/',views.singlep,name='singlep'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name = 'add_to_cart'),
    path("remove-cart/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("update-cart/<int:cart_item_id>/", views.update_cart, name="update_cart"),


    
]