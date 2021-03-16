from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# use classView instead of functionView to display list of objects, (must contain model and template_name -)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html - default template
    context_object_name = 'posts' # context name for model list - default name : object_list
    ordering = ['-date_posted']
    paginate_by = 5 # use default django pagination


# get posts by user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    # override get_queryset to only get a posts by certain user , specify user in url
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # kwargs will allow to access user on frontend
        return Post.objects.filter(author=user).order_by('-date_posted')


# use default template & object names
class PostDetailView(DetailView):
    model = Post


# Default template name - <app>/<model>_form - shared with update 
# LoginRequiredMixin - works like @login_required decorator for functionViews
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # override form_valid to avoid error - author is foreign key to user - assign it to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Default template name - <app>/<model>_form - shared with create 
# UserPassesTestMixin - to access route user must pass test in a test_func - only post author can update/delete
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # function for UserPassesTestMixin - current user == post.author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# UserPassesTestMixin - to access route user must pass test in a test_func - only post author can update/delete
# Default template name - <app>/<model>_confirm_delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # success redirect url

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})