from django.db import models
from django.db.models import CASCADE

from general_menu.models import TopProduct

class Product_list(models.Model):

    CLOTH_TYPE = (
        ("Clothes", "Clothes"),
        ("Shoes", "Shoes"),
        ("Pants", "Pants"),
    )

    name = models.CharField(max_length=100, verbose_name="Наименование одежды", null=True)
    image = models.ImageField(
        upload_to="images/", verbose_name="Загрузите фото одежды", null=True
    )
    about_book = models.TextField(verbose_name="Об одежде", null=True)
    cloth_type = models.CharField(
        null=True, max_length=20, choices=CLOTH_TYPE, verbose_name="Какой жанр"
    )

class ReviewsProduct(models.Model):
    review_product = models.ForeignKey(
        TopProduct, on_delete=CASCADE, related_name="reviews_books"
    )
    text = models.TextField()
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.points} - {self.review_product}"
