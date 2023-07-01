from rest_framework import serializers
from .models import Ads, Category, HashTag, AdsImage
from rest_framework.exceptions import ValidationError

"""Meta позволяет настроить различные аспекты модели,
такие как название таблицы базы данных, сортировка объектов,
разрешения доступа и другие параметры, связанные с моделью"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'


class AdsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsImage
        fields = 'id image'.split()


class AdsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    hash_tags = HashTagSerializer(many=True)
    images = AdsImageSerializer(many=True)

    class Meta:
        model = Ads
        fields = 'id images category category_name_list hash_tags hash_tag_name_list title'.split()


class AdsValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    text = serializers.CharField(required=False)
    is_active = serializers.BooleanField(default=True)
    price = serializers.FloatField(min_value=1, max_value=1000)
    phone = serializers.CharField(min_length=2, max_length=12)  # <-- проверка тут идет посимвольно
    category_id = serializers.IntegerField(min_value=1)
    hash_tags = serializers.ListField(child=serializers.IntegerField(min_value=1))

    # так как ListField принимает лист с любыми данными мы указываем
    # child который будет принимать только IntegerField

    def validate_category_id(self, category_id):  # 100
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id

    def validate_hash_tags(self, hash_tags):  # [1, 2, 100]                        без flat=True[(1,), (2,)]
        hash_tags_from_db = HashTag.objects.filter(id__in=hash_tags).values_list('id', flat=True)  # c flat=True [1, 2]
        if len(hash_tags_from_db) != len(hash_tags):  # если введенные id из хэштегов неверные тогда
            invalid_ids = set(hash_tags) - set(hash_tags_from_db)  # отнимаем тег пользователя от тега в базе
            raise ValidationError(f'Tag with id |{invalid_ids}| do not exist!')
        return hash_tags_from_db
