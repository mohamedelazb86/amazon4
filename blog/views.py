from django.shortcuts import render,redirect
from .models import Post,Review
from .forms import ReviewForm,PostForm

def post_list(request):

    posts=Post.objects.all()
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            form.save()
            return redirect('/blog/')
    else:
        form=PostForm()

    context={
        'posts':posts,
        'form':form,

    }
    return render(request,'blog/post_list.html',context)


def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    reviews=Review.objects.filter(post=post)

    if request.method =='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=post
            form.save()
            return redirect(f'/blog/{post.slug}')
    else:
        form=ReviewForm()

    context={
        'post':post,
        'reviews':reviews,
        'form':form,
    }


    return render(request,'blog/post_detail.html',context)
