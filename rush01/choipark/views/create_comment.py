from django.shortcuts import render, redirect
from django.views.generic import FormView
from ..forms import ArticleForm, CommentForm
from ..models import ArticleModel, CommentsModel

class CreateComment(FormView):
    commentform = CommentForm
    # def get(self, request, article_id):
        # article = ArticleModel.objects.get(id=article_id)
        # comments = CommentsModel.objects.all().filter(id=article_id)
        # # reply = Co
        # context = {
        #     'article' : article,
        #     'commentform' : self.commentform,
        #     'comments' : comments,
        #     #"replies" : ReplyModel.objects.all()
        # }
        # return render(request, 'view_article.html', context)

    def post(self, request, comment_id):
        comment = self.commentform(request.POST)
        if comment.is_valid():
            temp = comment.save(commit=False)
            temp.post = ArticleModel.objects.get(id = comment_id)
            temp.save()
        if request.POST.get('up_c') or request.POST.get('down_c'):
            comment = CommentsModel.objects.get(pk=request.POST.get('up_c') or request.POST.get('down_c'))
            if request.POST.get('up_c'):
                comment.upvote(request.user)
            else:
                comment.downvote(request.user)
        if request.POST.get('delete_c') :
            comment = CommentsModel.objects.get(pk=request.POST.get('delete_c'))
            if not (comment.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
                CommentsModel.objects.get(pk=request.POST.get('delete_c')).delete()
        return redirect('article_comment', comment_id)