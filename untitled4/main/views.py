from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.timezone import now
from django.views import View

from .models import Post, Comment, Tag, Category, Preference
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from .forms import UserRegisterForm, PostReportingForm, MakingCategoryForm, MakingTagForm, CommentForm
from django.contrib.auth.decorators import login_required



def home_view(request):
    template = loader.get_template("main.html")
    nav_Item = [123, 123]
    context = {
        'nav_Item': nav_Item
    }

    return HttpResponse(template.render(context, request))


def signIn_view(request):
    template = loader.get_template("sing_in_form_page.html")

    context = {}


    return HttpResponse(template.render(context, request))



def postdetail_view(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            newComment = Comment.objects.create(account=request.user, post=Post.objects.get(id=pk), date=now(), text=form.save(commit=False).text)
            newComment.save()

            messages.success(request, f'commented!', {'form': form})
            return redirect('postdetail', pk)
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        form = CommentForm()
        context = {
            'post': post,
        }

        return render(request, 'one_post_page.html', context)


def postlist_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        print(posts)
        context = {'post_list': posts}

        return render(request, 'posts_list_page.html', context)
    #return render(request, 'posts_list_page.html', )


def register(request):

    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! you are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required()
def profile(request):
    context = {}

    return render(request, 'users/profile.html', context)


@login_required()
def report(request):
    if request.method == 'POST':
        form = PostReportingForm(request.POST)

        if form.is_valid:

            newpost = form.save()
            newpost.reporter = request.user
            newpost.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Post {title}  Created by reporter {request.user}! you are now able find it in posts page')
            return redirect('posts')

    if request.method == 'GET':
            form = PostReportingForm()
            context = {'form': form}
            return render(request, 'modelForm/postReporting.html', context)


@login_required()
def tag(request):
    if request.method == "POST":
        form = MakingTagForm(request.POST)

        if form.is_valid():
            form.save()

            title = form.cleaned_data.get('title')
            messages.success(request, f'Tag {title} created!')
            return redirect('tagCreating')

    if request.method == "GET":
        form = MakingTagForm()
        context = {'form': form}
        return render(request, 'modelForm/tagCreating.html', context)


@login_required()
def category(request):
    if request.method == 'POST':
        form = MakingCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            context = {'form': form}

            messages.success(request, f'Category {title} created!', context)
            return redirect('categoryCreating')

    if request.method == 'GET':
        form = MakingCategoryForm()
        return render(request, 'modelForm/CategoryCreating.html', {'form': form})


class Tagdetail(View):
    def get(self, request, tag_id):
        tag = Tag.objects.get(id=int(tag_id))
        print(tag)
        posts = Post.objects.filter(tag=tag)
        context = {'post_list': posts}
        return render(request, 'posts_list_page.html', context)


class Categorydetail(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        posts = Post.objects.filter(category=category)
        context = {'post_list': posts}
        return render(request, 'posts_list_page.html', context)


@login_required
def postpreference(request, pk, userpreference):
    if request.method == "POST":
        eachpost = get_object_or_404(Post, id=pk)
        obj = ''
        valueobj = ''
        try:
            obj = Preference.objects.get(user=request.user, post=eachpost)
            valueobj = obj.value  # value of userpreference
            valueobj = int(valueobj)
            userpreference = int(userpreference)

            if valueobj != userpreference:
                obj.delete()
                upref = Preference()
                upref.user = request.user
                upref.post = eachpost
                upref.value = userpreference
                if userpreference == 1 and valueobj != 1:
                    eachpost.like += 1
                elif userpreference == 2 and valueobj != 2:
                    eachpost.like -= 1
                upref.save()
                eachpost.save()
                context = {'eachpost': eachpost,
                           'postid': pk}
                return redirect('postdetail', pk=pk)
            elif valueobj == userpreference:
                obj.delete()
                if userpreference == 1:
                    eachpost.like -= 1
                elif userpreference == 2:
                    pass
                eachpost.save()

                return redirect('postdetail', pk=pk)
        except Preference.DoesNotExist:
                        upref = Preference()
                        upref.user = request.user
                        upref.post = eachpost
                        upref.value = userpreference
                        userpreference = int(userpreference)
                        if userpreference == 1:
                                eachpost.like += 1
                        elif userpreference == 2:
                                  pass
                        upref.save()
                        eachpost.save()
                        context= {'eachpost': eachpost,
                          'postid': pk}
                        return redirect('postdetail', pk=pk)
        else:
                eachpost= get_object_or_404(Post, id=pk)
                context= {'eachpost': eachpost,
                          'postid': pk}
                return redirect('postdetail', pk= pk)






