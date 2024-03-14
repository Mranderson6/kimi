from django.shortcuts import render, get_object_or_404
from .models import BlogPost, itemImage

# Create your views here.
def home(request):
    head_post  = BlogPost.objects.all().order_by('-date_posted')[:1]
    # head_post_img = itemImage.objects.filter(item=head_post)
    all_posts = BlogPost.objects.all()
    return render(request, 'blog/blog.html', locals())

def blogDetails(request, id):
    current_one = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/blogDetails.html',locals())