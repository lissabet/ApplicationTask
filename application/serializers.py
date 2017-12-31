from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer
from .models import Category, Items, AttachmentImage
from rest_framework import filters


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('title', 'category', 'description' )


class ItemCteateSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()




    def create(self, validated_data):
        attachment = AttachmentImage(image=validated_data['image'], title=validated_data['image'])
        attachment.save()

        item = Items(title=validated_data['title'], description=validated_data['description'],
                                                                                      category = validated_data['category'],
                     )
        item.save()

        item.image = attachment
        item.save()
        return item




    class Meta:
        model = Items
        fields = ('title', 'category', 'description','image')