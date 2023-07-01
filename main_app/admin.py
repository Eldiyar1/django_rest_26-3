from django.contrib import admin
from .models import Ads, HashTag, Category, AdsImage

admin.site.register(Ads)
admin.site.register(HashTag)
admin.site.register(Category)
admin.site.register(AdsImage)


