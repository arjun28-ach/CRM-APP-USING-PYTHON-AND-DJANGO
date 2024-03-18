from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user"),
    path('account/', views.accountSettings, name="account"),
    path('products/', views.products, name="products"),
    path('customer/<str:primary_key>/', views.customer, name="customer"),
    path('customer/<int:customer_id>/', views.customer, name='customer_detail'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    #path('update_order/<str:primary_key>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:primary_key>/', views.deleteOrder, name="delete_order"),
    path('update_customer/<int:pk>/', views.updateCustomer, name='update_customer'),
    #path('create_order/<int:customer_id>/', views.createOrder, name='create_order'),
    path('customer/<int:customer_id>/create_order/', views.createOrder, name='create_order'),
    path('order/<int:primary_key>/update/', views.updateOrder, name='update_order'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('calculator/', views.calculatorPage, name="calculator"), 
    path('search_customer/', views.search_customer, name='search_customer'),
    path('search_product/', views.search_product, name='search_product'),
    path('my_stock/', views.my_stock, name='my_stock'),
    path(
        'reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
        name="reset_password"
    ),
    path(
        'reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"
    ),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"
    ),
    
       
]
