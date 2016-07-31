from django.shortcuts import render
from .models import Post
from.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts ': posts})
  

