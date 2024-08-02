from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import Anime
from .form import ReviewsForm

class HomeView(View):
    def get(self, request):
        animes = Anime.objects.all()
        return render(request, "ams/home_page.html", {'anime_list': animes})
    
    
class AnimePage(View):
    def get(self, request, pk):
        anime = Anime.objects.get(id=pk)
        return render(request, "ams/anime_page.html", {'anime': anime})
    

class AddReviews(View):
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.anime_id = pk
            form.save()
        return redirect(f"/{pk}")