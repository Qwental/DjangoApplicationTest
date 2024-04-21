from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)  # Поле может быть пустым

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal +-= float
    quantity = models.PositiveIntegerField(default=0)  # int >= 0!
    image = models.ImageField(upload_to='products/images')
    category = models.ForeignKey(to=ProductCategory,
                                 on_delete=models.CASCADE)  # для связи с ProductCategory # ПРОТЕКТ - категорию нельзя будет удалить пака  объекты тоже не будут удалены

    # CASKADE сносит всю категорию СО ВСЕМИ ТОВАРАМИ нахуй
    def __str__(self):
        return f'Товар: {self.name} | Категория: {self.category.name}'
