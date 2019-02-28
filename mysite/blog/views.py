from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def post_list(request):
    post_list=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context={'post_list':post_list}
    return render(request,'blog/post_list.html',context)
