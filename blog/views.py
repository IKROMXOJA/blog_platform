from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        author = User.objects.first()  # vaqtinchalik birinchi userga yoziladi

        Post.objects.create(title=title, content=content, image=image, author=author)
        return redirect('index')

    return render(request, 'post_create.html')
