# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import WatchList, StreamPlatform, Review
# from .serializer import WatchListSerializer, StreamPlatformSerializer,ReviewSerializer
# from rest_framework import status


# # Create your views here.
# class WatchListAPI(APIView):
#     def get(self,request):
#         obj= WatchList.objects.all()
#         serializer = WatchListSerializer(obj, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self, request):
#         data=request.data
#         print(request.data)
#         serializer= WatchListSerializer(data=data)
#         print(list(serializer.get_fields().keys()))
#         if not serializer.is_valid():
#             return Response({
#                 'status':False,
#                 'message':serializer.errors
#             },status=status.HTTP_400_BAD_REQUEST)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         data=request.data
#         obj= WatchList.objects.get(id=pk)
#         serializer=WatchListSerializer(obj,data=data)
#         if not serializer.is_valid():
#             return Response({
#                 'status':False,
#                 'message':serializer.errors
#             },status=status.HTTP_400_BAD_REQUEST)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)
    
#     def patch(self, request,pk):
#         data=request.data
#         obj= WatchList.objects.get(id=pk)
#         serializer= WatchListSerializer(obj, data=data,partial=True)
#         if not serializer.is_valid():
#                 return Response({
#                     'status':False,
#                     'message':serializer.errors
#                 },status=status.HTTP_400_BAD_REQUEST)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)

#     def delete(self,request, pk):
#         obj=WatchList.objects.get(id=pk)
#         obj.delete()
#         return Response({
#             'status':True,
#             'message':'Delete Successfully'
#         },status=status.HTTP_200_OK)
    
    
         
# class StreamPlatformAPI(APIView):
    
#     def get(self,request):
#         obj= StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(obj, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self, request):
#         data=request.data
#         serializer= StreamPlatformSerializer(data=data)
#         if not serializer.is_valid():
#             return Response({
#                 'status':False,
#                 'message':serializer.errors
#             },status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         data=request.data
#         obj= StreamPlatform.objects.get(id=pk)
#         serializer=StreamPlatformSerializer(obj,data=data)
#         if not serializer.is_valid():
#             return Response({
#                 'status':False,
#                 'message':serializer.errors
#             },status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)
    
#     def patch(self, request,pk):
#         data=request.data
#         obj= StreamPlatform.objects.get(id=pk)
#         serializer= StreamPlatformSerializer(obj, data=data,partial=True)
#         if not serializer.is_valid():
#                 return Response({
#                     'status':False,
#                     'message':serializer.errors
#                 },status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)

#     def delete(self,request, pk):
#         obj=StreamPlatform.objects.get(id=pk)
#         obj.delete()
#         return Response({
#             'status':True,
#             'message':'Delete Successfully'
#         },status=status.HTTP_200_OK)


# class ReviewAPI(APIView):
    
#     def get(self,request):
#         obj= Review.objects.all()
#         serializer = ReviewSerializer(obj, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self, request):
#         data=request.data
#         serializer= ReviewSerializer(data=data)
#         if not serializer.is_valid():
#             return Response({
#                 'status':False,
#                 'message':serializer.errors
#             },status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         data=request.data
#         obj= Review.objects.get(id=pk)
#         serializer=ReviewSerializer(obj,data=data)
#         if not serializer.is_valid():
#             return Response({
#                 'status':False,
#                 'message':serializer.errors
#             },status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)
    
#     def patch(self, request,pk):
#         data=request.data
#         obj= Review.objects.get(id=pk)
#         serializer= ReviewSerializer(obj, data=data,partial=True)
#         if not serializer.is_valid():
#                 return Response({
#                     'status':False,
#                     'message':serializer.errors
#                 },status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({
#                 'status':True,
#                 'message':'User Created'
#             },status=status.HTTP_200_OK)

#     def delete(self,request, pk):
#         obj=Review.objects.get(id=pk)
#         obj.delete()
#         return Response({
#             'status':True,
#             'message':'Delete Successfully'
#         },status=status.HTTP_200_OK)
    

from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from .models import WatchList, StreamPlatform, Review
from .serializer import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer, RegisterSerializer, LoginSerializer
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import WatchListFilter
from django.contrib.auth.models import User
from django.contrib.auth import login
from .permissions import IsReviewUserOrReadOnly


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            'status': True,
            'message': 'Logged in successfully'
        }, status=status.HTTP_200_OK)



class RegisterAV(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'status': True,
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)



# ---------- Level 1: StreamPlatform ----------

class StreamPlatformListCreateAV(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class StreamPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# ---------- Level 1: WatchList ----------

class WatchListListCreateAV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    filterset_class = WatchListFilter
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields=['title','storyline']

    pagination_class=PageNumberPagination
    page_size= 3
    page_size_query_param = 'page_size'
    max_page_size = 5

class WatchListDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


# ---------- Level 2: Review ----------

class ReviewListAV(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewCreateAV(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        # validation (rating range + duplicate check) already ran in serializer.is_valid()
        serializer.save()


class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]