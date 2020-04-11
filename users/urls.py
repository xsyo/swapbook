from django.urls import path

from .views import CustomUserDetailView, CustomUserUpdateView, Index

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(), name='user_update'),
    path('', Index.as_view(), name='index'),
]
