from django.urls import path
from .views import ListingListCreate, ListingDetail

urlpatterns = [
    path('listings/', ListingListCreate.as_view(), name='listing-list-create'),
    path('listings/<int:pk>/', ListingDetail.as_view(), name='listing-detail'),
]