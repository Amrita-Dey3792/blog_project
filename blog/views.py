from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.db import connections
from .forms import PostForm
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import connections
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all() # SELECT * FROM posts;

    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


class HomeView(ListView):
    model = Post # Post.objects.all()
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # This method is called to get the list of posts 

        # (N+1) Query Problem
        posts = Post.objects.filter(author__name__icontains='John') 

        print(self.request.user.is_authenticated) # True or False

        for post in posts:
            print(post.author.name) # N Queries 

        for query in connections['default'].queries:
            print("Hello")
            print(query['sql'])

        return posts


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse("Post not found", status=404)
    
    context = {
        'post': post
    }
    return render(request, 'post-details.html', context)



def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        # print(form.cleaned_data.get('title'))
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form)
    
    

def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        
        if request.method == "POST":
            post.delete()
            return redirect("home")

        return render(request, "delete_confirmation.html")
    except Post.DoesNotExist:
        return HttpResponse("Post not found", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    

class DeletePostView(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('home')

    # def delete(self, request, *args, **kwargs):
    #     print("Deleting post...")
    #     messages.success(request, "Post deleted successfully!")
    #     return super().delete(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.error(self.request, "Post deleted successfully!")    
        return super().form_valid(form)
    
@login_required
def update_post(request, pk):

    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = PostForm(instance=post)

    return render(request, 'post_form.html', {'form': form})

