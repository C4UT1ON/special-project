from reservation_system import views
from django.urls import path

urlpatterns = [
    path('items', views.ItemList.as_view()),
    path('items/<int:pk>', views.ItemObject.as_view()),
    path('bookings', views.BookingList.as_view()),
    path('bookings/<int:pk>', views.BookingObject.as_view())
]
