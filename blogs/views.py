from django.views.generic import ListView, DetailView
from furniture_main.models import Article 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PostCreateForm
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from furniture_main.forms import CommentForm


class BlogListView(ListView):
    model = Article
    template_name = 'blog.html'     
    context_object_name = 'posts'          
    ordering = ['-published_at']           
    paginate_by = 10                       

class BlogDetailView(DetailView):
    model = Article
    template_name = 'blogpost.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # или любая другая логика перенаправления

        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
        return redirect('blog:detail', pk=self.object.pk)
     

class PostCreateView(CreateView):
    model = Article
    form_class = PostCreateForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('blog_list') 
    
class VideoView(TemplateView):
    template_name = 'video.html'
