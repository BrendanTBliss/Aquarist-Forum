from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post, Profile, Category
from .forms import Post_Form, Profile_Form, User_Form, SignUpForm, Profile_User_Form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string

from .forms import SignUpForm
from .tokens import account_activation_token

# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')

def api(request):
    return JsonResponse({"status": 200})

# def profile(request):
#     return render(request, 'profile/detail.html')

# --- Posts Index ---
@login_required
def posts_index(request):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            # save(commit=False) will just make a copy/instance of the model
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            # save() to the db
            new_post.save()
            return redirect('posts_index')
    post = Post.objects.filter(user=request.user)
    posts = Post.objects.all()
    post_form = Post_Form()
    context = {'post': post, 'post_form': post_form, 'posts': posts}
    return render(request, 'posts/index.html', context)

# --- Post Detail ---
@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

@login_required 
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = Post_Form(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts_detail', post_id=post.id)
        else:
            post_form = Post_Form(instance=post)
            context = {'post': post, 'post_form': post_form}
            return render(request, 'posts/edit.html', context)

# --- Post delete ---

@login_required
def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect("posts_index")


        
# --- Profile Detail ---
def profile_detail(request):
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user = user)
    context = {'posts': posts}
    return render(request, 'profile/profile.html', context)


# --- Profile delete ---
@login_required
def profile_delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("home")

def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')


def signup(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# --- Login ---
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home', user_id=user.id)
    else:
        return redirect('home')

@login_required 
def profile_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        # user_form = User_Form(request.POST, instance=user)
        profile_form = Profile_Form(request.POST, instance=user.profile)
        profile_user_form = Profile_User_Form(request.POST, instance=user)
        if profile_form.is_valid() and profile_user_form.is_valid():
            profile_form.save()
            profile_user_form.save()
            # user_form.save()
            return redirect('profile')
        else:
            user_form = User_Form(instance=user)
            profile_form = Profile_Form(instance=user.profile)
            profile_user_form = Profile_User_Form(instance=user)
            context = {'user': user, 'user_form': user_form, 'profile_form': profile_form, 'profile_user_form': profile_user_form}
            return render(request, 'profile/edit.html', context)


# --- Category Index ---
def categories_index(request):
    profile = Profile.objects.all()
    categories = Category.objects.all()
    post = Post.objects.all()
    context = {'categories': categories, 'posts': post, 'profile': profile}
    return render(request, 'categories/index.html', context)

# --- Category Detail ---
def categories_detail(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category_id=category.id)
    post = Post.objects.all()
    post_form = Post_Form()
    context = {'login': AuthenticationForm(), 'post': post, 'signup': UserCreationForm(), 'category': category, 'categories': categories, 'post_form': post_form, 'posts': posts.order_by("created_at")}
    return render(request, 'categories/detail.html', context)
