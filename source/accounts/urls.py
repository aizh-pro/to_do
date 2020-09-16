from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import register_view, UserDetailView, UserListView, UserChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('accounts/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='change'),
]