from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='indexpage'),
    path('cart/',views.cart,name='cartpage'),
    path('shop/',views.view_products,name='shoppage'),
    path('register/',views.register,name='registerpage'),
    path('login/',views.logins,name='loginpage'),
    path('nav',views.nav,name='navpage'),
    path('logout',views.handle_logout,name='logout'),
    
    path('add_to_cart/<int:i>',views.add_to_cart,name='add_to_cart'),
    path('removeall',views.removeall_from_cart,name='removeall'),
    path('removeitem/<int:item_id>',views.remove_item,name='removeitem'),
    path('about',views.about,name='about'),
    path('blog',views.about,name='blog'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services')
    
    
    
]
