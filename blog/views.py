from django.shortcuts import render,redirect
from .models import Blog,Comment,Like

# Create your views here.
def recentblogs(request):
    pass

def allblogs(request):
    blogs = Blog.objects.all()
    for blog in blogs:
        no_of_likes=len(list(Like.objects.filter(parent_blog=blog)))
        no_of_comments=len(list(Comment.objects.filter(parent_blog=blog)))
        blog.no_of_likes=no_of_likes
        blog.no_of_comments=no_of_comments
        blog.save()
    blogs = Blog.objects.all()
    return render(request,'blog/index.html',{'blogs':blogs})

def detailedblog(request,pk):
    if request.user.is_anonymous:
        return redirect('/blogs/allblogs')
    blog=Blog.objects.get(id=pk)
    no_of_likes = len(list(Like.objects.filter(parent_blog=blog)))
    no_of_comments = len(list(Comment.objects.filter(parent_blog=blog)))
    blog.no_of_likes = no_of_likes
    blog.no_of_comments = no_of_comments
    blog.blog_views=blog.blog_views+1
    blog.save()
    blog = Blog.objects.get(id=pk)
    comments=Comment.objects.filter(parent_blog=blog)
    liked=Like.objects.filter(reader=request.user).filter(parent_blog=blog).exists()
    return render(request,'blog/blog.html',{'blog':blog,'comments':comments,'liked':liked})

def postcomments(request,pk):
    if request.user.is_anonymous:
        return redirect('/blogs/allblogs')
    if request.method == 'POST':
        comment=request.POST.get('comment')
        new_comment=Comment(body=comment,reader=request.user,parent_blog=Blog.objects.get(id=pk))
        new_comment.save()
    blog = Blog.objects.get(id=pk)
    blog.blog_views=blog.blog_views-1
    blog.save()
    return redirect(f'/blogs/detailedblog/{pk}')

def hitlike(request,pk):
    if request.user.is_anonymous:
        return redirect('/blogs/allblogs')

    blog= Blog.objects.get(id=pk)
    if Like.objects.filter(reader=request.user).filter(parent_blog=blog).exists():
        like=Like.objects.filter(reader=request.user).filter(parent_blog=blog)
        like.delete()
    else:
        new_like=Like(parent_blog=blog,reader=request.user)
        new_like.save()
        
    blog.blog_views=blog.blog_views-1
    blog.save()
    return redirect(f'/blogs/detailedblog/{pk}')
