from django.shortcuts import render
from .models import *
from django.http import Http404
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# Create your views here.


class ItemList(APIView):
    @csrf_exempt
    def get(self, request):
        items = Item.objects.all()
        return Response(ItemSerializer(items, many=True).data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemObject(APIView):
    @csrf_exempt
    def get_item(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, pk):
        item = self.get_item(pk)
        return Response(ItemSerializer(item).data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = ItemSerializer(self.get_item(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_item(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookingList(APIView):
    @csrf_exempt
    def get(self, request):
        bookings= Booking.objects.all()
        return Response(BookingSerializer(bookings, many=True).data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self,request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingObject(APIView):
    @csrf_exempt
    def get_booking(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    @csrf_exempt
    def get(self, request, pk):
        booking = self.get_booking(pk)
        return Response(booking, status=status.HTTP_200_OK)

    @csrf_exempt
    def put(self, request, pk):
        serializer = BookingSerializer(self.get_booking(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk):
        self.get_booking(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




