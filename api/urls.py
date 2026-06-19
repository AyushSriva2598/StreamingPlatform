# from django.contrib import admin
# from django.urls import path
# from Home.views import WatchListAPI, StreamPlatformAPI, ReviewAPI

# urlpatterns = [
#     path('watchlist/',WatchListAPI.as_view()),
#     path('watchlist/<int:pk>/',WatchListAPI.as_view()),
#     path('streamplatform/',StreamPlatformAPI.as_view()),
#     path('streamplatform/<int:pk>/',StreamPlatformAPI.as_view()),
#     path('review/',ReviewAPI.as_view()),
#     path('review/<int:pk>/',ReviewAPI.as_view())
# ]


from django.urls import path
from Home.views import (
    StreamPlatformListCreateAV,
    StreamPlatformDetailAV,
    WatchListListCreateAV,
    WatchListDetailAV,
    ReviewListAV,
    ReviewCreateAV,
    ReviewDetailAV,
)

urlpatterns = [
    # StreamPlatform
    path('stream/', StreamPlatformListCreateAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # WatchList
    path('watchlist/', WatchListListCreateAV.as_view(), name='watchlist-list'),
    path('watchlist/<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-detail'),

    # Review
    path('watchlist/<int:pk>/review/', ReviewListAV.as_view(), name='review-list'),
    path('watchlist/<int:pk>/review-create/', ReviewCreateAV.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
]