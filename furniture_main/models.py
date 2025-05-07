from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    # ваша модель статьи
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    summary = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="Статья")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        ordering = ['-date']  # сортировка по убыванию даты

    def __str__(self):
        return f'Комментарий к "{self.post.title}" от {self.author.username}'
