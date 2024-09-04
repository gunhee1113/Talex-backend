from django.urls import path
from .views import RegisterView, UserProfileView, UserTalentsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('<int:user_id>/talents/', UserTalentsView.as_view(), name='user-talents'),
]