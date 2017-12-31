from django.db import models
import uuid
import datetime
import os


def content_file_name(instance, filename):
    now = datetime.datetime.now()
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return '/'.join(['%d' % now.year, '%d' % now.month, '%d' % now.day, filename])


class AttachmentImage(models.Model):
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.extension = os.path.splitext(self.image.path)[1][1:]
        return super(AttachmentImage, self).save(force_insert, force_update, using, update_fields)

    title = models.CharField(
        verbose_name='Title',
        max_length=255,
        blank=True,
        null=True
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=content_file_name
    )


    class Meta:
        verbose_name = "Attachment image"
        verbose_name_plural = "Attachment images"



class Category(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)

    class Meta:
        app_label = "application"
        verbose_name = "Category"
        verbose_name_plural = "Categories"




class Items(models.Model):
    def __str__(self):
        return self.title

    category = models.ForeignKey(
        Category,
        related_name='item_category',
        verbose_name='category',
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True
    )

    image = models.ManyToManyField(
        AttachmentImage,
        related_name='item_image',
        verbose_name='image',
        default=None,
        blank=True,
    )

    title = models.CharField(
        verbose_name='title',
        max_length=255,
    )

    description = models.TextField(
        verbose_name='description',
        max_length=255,
    )

    class Meta:
        app_label = "application"
        verbose_name = "Item"
        verbose_name_plural = "Items"
