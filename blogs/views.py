from dataclasses import field
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,PostLikes
from .forms import PostCreateForm

    
def PostListView(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_queryset(self):
        user=get_object_or_404( User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') 
    

def PostDetailView(request,pk):
    print(request.POST)
    post = Post.objects.get(id = pk)
    post_liked = None
    if request.POST.get('like') and request.method == 'POST':
            post_liked = Post.objects.get(id = request.POST.get('like'))
            already_liked = PostLikes.objects.filter(user=request.user, post=post_liked).count()
            if already_liked == 0:
                like = PostLikes.objects.create(user=request.user,post = post_liked)
    elif request.POST.get('dislike') and request.method == 'POST':
            post_liked = Post.objects.get(id = request.POST.get('dislike'))
            already_liked = PostLikes.objects.filter(user=request.user, post=post_liked).count()
            if already_liked > 0:
                try:
                    dislike =  PostLikes.objects.get(user=request.user,post = post_liked).delete()
                except Exception as e:
                    print(e)
    if post_liked is not None:
            likes = PostLikes.objects.all().filter(post=post_liked).count()
            print(likes)
            context = {'likes':likes,'post':post}
            return render(request,'blog/post_detail.html',context)
    return render(request,'blog/post_detail.html',{'post':post})
    
    
    
def PostSearchView(request):
    print(request.GET)
    if request.method == 'GET':
        if request.GET.get('search_btn') == 'search':
            query = request.GET.get('search_bar')
            if query is not '':
                title_search = Post.objects.all().filter(title__icontains= query)
                content = Post.objects.all().filter(content__icontains=query)
                context = {'ontitle':title_search,'oncontent':content}
                return render(request,'blog/post_search.html',context)
    return render(request,'blog/post_search.html')
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_forms.html'
    context_object_name = "post"
    fields = ['title','content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    template_name = 'blog/post_forms.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class  PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        i = False
        if self.request.user == post.author:
            i= True
            return i
        return i

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
