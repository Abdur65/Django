# Django
from django.contrib.auth import views as auth_views
from django.urls import path

# restframework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, mymodel_view, LogoutView
from books.views import BookListView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("list/", BookListView.as_view(), name="list"),
    path('register/', RegisterView.as_view(), name='register'),
    path('restricted/', mymodel_view, name='mymodel_view'),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/logout/', LogoutView.as_view(), name="token_logout"),
]
