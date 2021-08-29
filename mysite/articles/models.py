from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


class Article(models.Model):
    title = models.CharField(max_length=200),
    slug = models.SlugField(unique=True, max_length=100),
    body = models.TextField(),
    date = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(default='default.png', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True, null=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return '{}/{}'.format(self.title, self.body, self.slug)

    def snippet(self):
        return self.body[:50] + '...'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
