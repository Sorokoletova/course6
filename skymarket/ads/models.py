from django.conf import settings
from django.db import models
from users.models import User



class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара")
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор объявления")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создания" )
    image = models.ImageField(upload_to='images/', verbose_name="Фото", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=1000, verbose_name="Комментарий")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments', verbose_name="Обьявление")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания комментарий")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
