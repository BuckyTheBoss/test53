from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import RegisterForm

from .models import Comment, Post

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    posts = Post.objects.all()
    comment = Comment.objects.get(id=1)
    return render(request, 'index.html', {'posts': posts, 'comment': comment})


class CreatePostView(CreateView):
    model = Post
    fields = '__all__' #['title', 'content']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user if self.request.user.is_authenticated else None
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class PostDetailView(DetailView):
    model = Post


def signup_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
      
        return render(request, 'signup.html', {'form': form})

        
