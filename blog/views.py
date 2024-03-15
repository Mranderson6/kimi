from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Categorie, blogComment, itemImage

# Create your views here.
def home(request):
    head_post  = BlogPost.objects.all().order_by('-date_posted')[:1]
    for post in head_post:
        postId = post
    sous_posts = BlogPost.objects.all().exclude(id=postId.id).order_by('-date_posted')[:3]
    categories = Categorie.objects.all()
    # head_post_img = itemImage.objects.filter(item=head_post)
    all_posts = BlogPost.objects.all().exclude(id=postId.id).order_by('?')
    return render(request, 'blog/blog.html', locals())

def blogDetails(request, id):
    current_one = get_object_or_404(BlogPost, id=id)
    other_posts = BlogPost.objects.all().exclude(id=current_one.id).order_by('-date_posted')[:3]

    if request.method == 'POST':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        blogComment.object.create(nom=nom, mail=email, message=message)
    return render(request, 'blog/blogDetails.html',locals())

def categoryDetails(request, id):
    current_one = get_object_or_404(Categorie, id=id)
    for post in current_one.blogpost_set.all():
        for image in post.itemimage_set.all():
            print(image.image.url)
    return render(request, 'blog/categoryDetails.html', locals())