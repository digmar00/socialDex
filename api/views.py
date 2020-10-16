from django.shortcuts import render
from social_network.models import Post
from django.http import JsonResponse
from django.utils import timezone


def api(request):
    return render(request, 'api/api.html')


def posts(request):
    response = []

    posts = Post.objects.filter().order_by('-datetime')

    # For each Post, I retrieve the most important information by saving it in a dictionary
    for p in posts:
        # The dictionary is appended to the "response" variable
        response.append(
            {
                'datetime': p.datetime,
                'content': p.content,
                'author': f"{p.user}",
                'hash': p.hash,
                'tx_id': p.tx_id
            }
        )

    return JsonResponse(response, safe=False)


def last_hour_posts(request):
    response = []

    # I get the datetime value for exactly one hour ago
    one_hour_ago = timezone.now() - timezone.timedelta(hours=1)
    posts = Post.objects.filter(datetime__gte=one_hour_ago)

    # For each Post, I retrieve the most important information by saving it in a dictionary
    for p in posts:
        # The dictionary is appended to the "response" variable
        response.append(
            {
                'datetime': p.datetime,
                'content': p.content,
                'author': f"{p.user}",
                'hash': p.hash,
                'tx_id': p.tx_id
            }
        )

    return JsonResponse(response, safe=False)


def last_day_posts(request):
    response = []

    # I get the datetime value for exactly 24 hours ago
    one_day_ago = timezone.now() - timezone.timedelta(hours=24)
    posts = Post.objects.filter(datetime__gte=one_day_ago)

    # For each Post, I retrieve the most important information by saving it in a dictionary
    for p in posts:
        # The dictionary is appended to the "response" variable
        response.append(
            {
                'datetime': p.datetime,
                'content': p.content,
                'author': f"{p.user}",
                'hash': p.hash,
                'tx_id': p.tx_id
            }
        )

    return JsonResponse(response, safe=False)


def string_appearances(request):
    appearances = 0

    string = request.GET['string']
    posts = Post.objects.filter().order_by('-datetime')

    for p in posts:
        if string in p.content:
            appearances += 1

    return JsonResponse(appearances, safe=False)
