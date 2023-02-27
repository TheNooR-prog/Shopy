from django.db import models
import uuid
import os


class Post(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('posts/%Y/%m/%d/', new_filename)

    category = models.CharField(max_length=50)
    name = models.CharField(unique=True, max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True)
    text = models.TextField()
    quote = models.TextField(max_length=500, blank=True)
    author = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    main_photo = models.ImageField(upload_to=get_file_name)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    home_photo = models.ImageField(upload_to=get_file_name)
    on_homepage = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.update_time} | {self.category}: {self.name}'

    class Meta:
        ordering = ('-update_time', )


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class ItemType(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('item_types/%Y/%m/%d/', new_filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Look(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('looks/%Y/%m/%d/', new_filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Item(models.Model):
    name = models.CharField(unique=True, max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=50)
    product_code = models.CharField(unique=True, max_length=8)
    description = models.TextField(blank=True)
    # photo
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    look = models.ForeignKey(Look, on_delete=models.SET_NULL, blank=True, null=True)
    # size
    # colour

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        index_together = (('id', 'slug'), )