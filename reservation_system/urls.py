<<<<<<< HEAD
from reservation_system import views
from django.urls import path

urlpatterns = [
    path('items', views.ItemList.as_view()),
    path('items/<int:pk>', views.ItemObject.as_view()),
    path('bookings', views.BookingList.as_view()),
    path('bookings/<int:pk>', views.BookingObject.as_view())
=======
"""reservation_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('res/', include('resources.urls'))
>>>>>>> 9142a665114861ff7c76413fa1846192ce1e6da6
]
