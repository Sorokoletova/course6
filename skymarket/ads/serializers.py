from rest_framework import serializers
from ads.models import Ad, Comment
from phonenumber_field import serializerfields



# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")


    class Meta:
        model = Comment
        fields = ("pk", "text", "ad_id", "author_id", "author_first_name", "author_last_name")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    phone = serializerfields.PhoneNumberField(source='author.phone', read_only=True)
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")

    class Meta:
        model = Ad
        fields = ('pk',
                  'image',
                  'title',
                  'price',
                  'phone',
                  'author_first_name',
                  'author_last_name',
                  'description',
                  'author_id',)

