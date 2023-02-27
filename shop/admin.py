from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from .models import Post, Category, ItemType, Look, Item, Size

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(ItemType)
admin.site.register(Look)
# admin.site.register(Item)

class ItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Item, ItemAdmin)
admin.site.register(Size)
