from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    ordering = ("name",)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Name: {self.name}"


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}"
