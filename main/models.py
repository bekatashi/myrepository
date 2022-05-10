from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', related_name='auhtor', on_delete=models.CASCADE,)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self): return f'{self.title}'
