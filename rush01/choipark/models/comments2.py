from django.conf import settings
from django.db import models
from ..models.articles import ArticleModel


class CommentsModel(models.Model):
    article = models.ForeignKey(ArticleModel,default='0', on_delete=models.CASCADE, related_name='comments')
    # 1 article : N comments
    content = models.TextField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    # 1 user : N comments
    date = models.DateTimeField(auto_now_add=True)

class ReplyModel(models.Model):
    content = models.TextField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    # 1 user : N comments
    date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey(
        CommentsModel,
        default='0',
        on_delete=models.CASCADE)