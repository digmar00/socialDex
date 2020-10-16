from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.models import Profile
from .forms import PostForm
from .models import Post


# I add the @login_required decorator to make sure that the user can see the homepage only if logged in
@login_required
def home(request):
    if request.user.is_authenticated:
        ip = get_client_ip(request)

        if (ip != request.user.profile.last_ip_used) & (request.user.profile.last_ip_used is not None):
            Profile.objects.filter(user=request.user).update(is_ip_changed=True)

        Profile.objects.filter(user=request.user).update(last_ip_used=ip)
    all_posts = Post.objects.all().order_by('-datetime')
    context = {
        'posts': all_posts
    }
    return render(request, 'social_network/home.html', context)


# I add the @login_required decorator to make sure that the user can add posts only if logged in
@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.write_on_chain()
            post.save()

            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'social_network/new_post.html',  {'form': form})


# I retrieve the user's IP address via the request.META.get() function
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
