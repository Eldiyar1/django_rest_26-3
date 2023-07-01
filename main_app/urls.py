from django.urls import path
from .views import test_api_view, ads_list_api_view, ads_detail_api_view
from .views import CategoryListAPIView, CategoryDetailAPIView, \
    HashTagAPIView, AdsListAPIView

urlpatterns = [
    path('test/', test_api_view),
    path('ads/<int:id>/', ads_detail_api_view),
    path('ads/', AdsListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),
    path('hash_tags/', HashTagAPIView.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('hash_tags/<int:id>/', HashTagAPIView.as_view({
        'get': 'retrieve', 'post': 'update', 'delete': 'destroy'
    }))
]
