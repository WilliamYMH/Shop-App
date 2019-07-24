from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.ProductList.as_view(), name="hello"),
    path("product/<int:pk>/", views.ProductDetail.as_view(), name="product_detail"),
    path("product/new", views.AddProduct.as_view(), name="new_product"),
    path("register/", views.CreateUser.as_view(), name="create_user"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
