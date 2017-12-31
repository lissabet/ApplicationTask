from django.contrib import admin
from .models import Category, Items
from .forms import ItemForm

class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    model = Items

admin.site.register(Category)
admin.site.register(Items, ItemAdmin)

# Register your models here.
