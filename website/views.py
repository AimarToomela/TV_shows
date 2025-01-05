from django.shortcuts import render, redirect, get_object_or_404
from .models import TVShow
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def featured_page(request):
    tv_shows = TVShow.objects.all()
    if request.user.is_authenticated:
        favorite_shows = request.user.favorites.all()
        for show in tv_shows:
            show.is_favorite = show in favorite_shows
    else:
        for show in tv_shows:
            show.is_favorite = False

    return render(request, 'featured.html', {'tv_shows': tv_shows})

def favorites_page(request):
    if request.user.is_authenticated:
        favorites = request.user.favorites.all()
    else:
        favorites=[]

    return render(request, 'favorites.html', {'favorites': favorites})

def details_page(request,show_id):
    show = get_object_or_404(TVShow, id=show_id)
    if request.user.is_authenticated and request.method == 'POST':
        request.user.favorites.add(show)
        return redirect('favorites')

    return render(request, 'details.html', {'show': show})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def add_to_favorites(request, show_id):
    if request.user.is_authenticated:
        show = get_object_or_404(TVShow, id=show_id)
        show.favorite_user.add(request.user)
        messages.success(request, "Successfully added to favorites!")
    else:
        messages.error(request, "You need to be logged in to add to favorites.")
    return redirect('featured')

def remove_from_favorites(request, show_id):
    if request.user.is_authenticated:
        show = get_object_or_404(TVShow, id=show_id)
        show.favorite_user.remove(request.user)
        return redirect('favorites')
    return redirect('login')
