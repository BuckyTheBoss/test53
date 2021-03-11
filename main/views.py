from django.shortcuts import render
from .models import Comment, Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    comment = Comment.objects.get(id=1)
    return render(request, 'index.html', {'posts': posts, 'comment': comment})
