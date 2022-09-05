from django.contrib import admin

from ads.models import Ad, Comment
admin.site.register(Ad)
admin.site.register(Comment)


# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

