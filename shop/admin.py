from django.contrib import admin
from .models import Post, Category, ItemType, Look, Item

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(ItemType)
admin.site.register(Look)
admin.site.register(Item)