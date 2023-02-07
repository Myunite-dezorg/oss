from django.urls import path
from .views import UserProfileListView, UserProfileDetailView, UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView

app_name = 'profiles'

urlpatterns = [
    path('', UserProfileListView.as_view(), name='list'),
    path('<str:unique_id>/', UserProfileDetailView.as_view(), name='detail'),
    path('create/', UserProfileCreateView.as_view(), name='create'),
    path('<str:unique_id>/update/', UserProfileUpdateView.as_view(), name='update'),
    path('<str:unique_id>/delete/', UserProfileDeleteView.as_view(), name='delete'),
    path('dashboard/', UserProfileDetailView.as_view(), name='dashboard'),
]