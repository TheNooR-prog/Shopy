from django.db import models

# Create your models here.
class Post(models.Model):
    # category
    # name
    # slug
    # text
    # subtext
    # add_time
    # update_time
    # main_photo
    # position
    # is_visible
    # home_photo
    # on_homepage
    pass

class Category(models.Model):
    # name
    # position
    # is_visible
    pass

class ItemType(models.Model):
    # name
    # photo
    # position
    # is_visible
    pass

class Look(models.Model):
    # name
    # photo
    # position
    # is_visible
    pass

class Item(models.Model):
    # name
    # slug
    # price
    # brand
    # product_code
    # description
    # photo
    # position
    # is_visible
    # is_trending
    # category
    # look
    # size
    # colour
    pass

