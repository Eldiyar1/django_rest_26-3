from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ads, Category, HashTag
from .serializers import AdsSerializer, AdsValidateSerializer, \
    CategorySerializer, HashTagSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class HashTagAPIView(ModelViewSet):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class AdsListAPIView(ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def post(self, request, *args, **kwargs):
        serializer = AdsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)  # <--Выдает ошибку клиенту автоматичеки
        name = serializer.validated_data.get('name')
        text = serializer.validated_data.get('text')
        is_active = serializer.validated_data.get('is_active')
        price = serializer.validated_data.get('price')
        phone = serializer.validated_data.get('phone')
        category_id = serializer.validated_data.get('category_id')
        hash_tags = serializer.validated_data.get('hash_tags')
        ads = Ads.objects.create(title=name, description=text, is_active=is_active,
                                 price=price, phone=phone, category_id=category_id, )
        ads.hash_tags.set(hash_tags)
        ads.save()
        return Response(data=AdsSerializer(ads).data)


# декоратор @api_view помогает нам определить какой HTTP запрос будет обрабатываться
@api_view(['GET', 'POST'])
def ads_list_api_view(request):
    print(request.user)
    if request.method == 'GET':
        """ Получаем список всех обьектов модели"""
        ads_list = Ads.objects.all()

        """ Сериализуем объекты ads_list в формат JSON """
        ads_json = AdsSerializer(instance=ads_list, many=True).data

        """ Return dict objects by JSON file """
        return Response(data=ads_json)
    elif request.method == 'POST':
        serializer = AdsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)  # <--Выдает ошибку клиенту автоматичеки
        name = serializer.validated_data.get('name')
        text = serializer.validated_data.get('text')
        is_active = serializer.validated_data.get('is_active')
        price = serializer.validated_data.get('price')
        phone = serializer.validated_data.get('phone')
        category_id = serializer.validated_data.get('category_id')
        hash_tags = serializer.validated_data.get('hash_tags')
        ads = Ads.objects.create(title=name, description=text, is_active=is_active,
                                 price=price, phone=phone, category_id=category_id, )
        ads.hash_tags.set(hash_tags)
        ads.save()
        return Response(data=AdsSerializer(ads).data)


@api_view(['GET', 'PUT', 'DELETE'])
def ads_detail_api_view(request, id):
    try:
        """ GET ads item"""
        item = Ads.objects.get(id=id)
    except Ads.DoesNotExist:
        return Response(data={'error': 'Ads not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        """ Ads item serialize to dict """
        ads_json = AdsSerializer(instance=item).data

        """ Return dict by JSON file """
        return Response(data=ads_json)
    elif request.method == "DELETE":
        item.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = AdsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.title = request.data.get('name')
        item.description = request.data.get('description')
        item.phone = request.data.get('phone')
        item.is_active = request.data.get('is_active')
        item.price = request.data.get('price')
        item.category_id = request.data.get('category_id')
        item.hash_tags.set(request.data.get('hash_tags'))
        item.save()
        return Response(data=AdsSerializer(item).data)


@api_view(['GET'])
def test_api_view(request):
    """ Logic """
    data_dict = {
        'text': 'Hello World',
        'int': 1000,
        'float': 2.5,
        'bool': True,
        'list': [1, 2, 3],
        'dict': {'key': 'value'},
    }
    return Response(data=data_dict)
