from django.urls import path, include
from main import views
urlpatterns = [
    path('products/', views.ProductsView.as_view()),
    path('products/<int:pk>/', views.ProductsDetailView.as_view()),
    path('products/create/', views.ProductCreateView.as_view()),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view()),
    path('users/register/', views.UserRegistrationView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
    path('users//rest-auth/', include('rest_auth.urls')),
    path('users/logout/', views.CustomLogOutView.as_view())
]
