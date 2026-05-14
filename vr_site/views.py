from django.shortcuts import render, redirect
from .forms import VRReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import json
from .models import VRReview, ReviewLike


@require_POST
@login_required
def like_review(request):
    """Обработка AJAX-запроса на постановку/снятие лайка/дизлайка"""
    data = json.loads(request.body)
    review_id = data.get("review_id")
    action = data.get("action")  # 'like' или 'dislike'
    review = VRReview.objects.get(id=review_id)
    user = request.user

    existing = ReviewLike.objects.filter(user=user, review=review).first()

    if existing:
        # Если уже есть голос
        if (action == "like" and existing.type == ReviewLike.LIKE) or (
            action == "dislike" and existing.type == ReviewLike.DISLIKE
        ):
            existing.delete()  # отмена
        else:
            existing.type = ReviewLike.LIKE if action == "like" else ReviewLike.DISLIKE
            existing.save()
    else:
        # Новый голос
        ReviewLike.objects.create(
            user=user,
            review=review,
            type=ReviewLike.LIKE if action == "like" else ReviewLike.DISLIKE,
        )

    return JsonResponse(
        {
            "likes": review.likes_count,
            "dislikes": review.dislikes_count,
        }
    )


def get_all_likes(request):
    """Возвращает актуальные счётчики лайков для всех отзывов (JSON)"""
    reviews = VRReview.objects.all()
    data = {}
    for review in reviews:
        data[review.id] = {
            "likes": review.likes_count,
            "dislikes": review.dislikes_count,
        }
    return JsonResponse(data)


def index(request):
    reviews = VRReview.objects.all().order_by("-created_at")  # все отзывы, новые сверху
    if request.method == "POST":
        form = VRReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = VRReviewForm()
    return render(request, "vr_site/index.html", {"form": form, "reviews": reviews})


def gallery(request):
    return render(request, "vr_site/gallery.html")


def experiences(request):
    return render(request, "vr_site/experiences.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Аккаунт {username} создан!")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "vr_site/register.html", {"form": form})
