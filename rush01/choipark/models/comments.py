from django.conf import settings
from django.db import models
from ..models import *


class CommentsModel(models.Model):
    article = models.ForeignKey(ArticleModel,default='0', on_delete=models.CASCADE)
    # 1 article : N comments
    content = models.TextField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    # 1 user : N comments
    date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey(
        'self', 
        blank=True, 
        null=True, 
        related_name='comments',
        on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvotes_comment')
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvotes_comment')

    def upvote(self, user):
        if self.downvotes.filter(id=user.id).count():
            self.downvotes.remove(user)
        if self.upvotes.filter(id=user.id).count():
            self.upvotes.remove(user)
        else:
            self.upvotes.add(user)

    def downvote(self, user):
        if self.upvotes.filter(id=user.id).count():
            self.upvotes.remove(user)
        if self.downvotes.filter(id=user.id).count():
            self.downvotes.remove(user)
        else:
            self.downvotes.add(user)
