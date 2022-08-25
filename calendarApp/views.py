from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .calSerializers import CalSerializer
from .models import Cal


class CalList(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        cal = Cal.objects.all()
        serializer = CalSerializer(cal, many=True)
        return Response(serializer.data)

class CalDetail(APIView):
    def get_object(self, pk):
        try:
            return Cal.objects.get(pk=pk)
        except Cal.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        cal = self.get_object(pk)
        serializer = CalSerializer(cal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cal = self.get_object(pk)
        serializer = CalSerializer(cal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cal = self.get_object(pk)
        cal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
