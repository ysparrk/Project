from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    context = {'movies' : movies}
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movies = form.save()
            return redirect('movies:detail', movies.pk)
    
    else:
        form = MovieForm()
    context = {'form' : form}
    return render(request, 'movies/create.html', context)

@require_http_methods(['GET'])
def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {'movies' : movies}
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movies = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movies.pk)
    else:
        form = MovieForm(instance=movies)

    context = {'form' : form, 'movies' : movies}
    return render(request, 'movies/update.html', context)


@require_http_methods(['POST'])
def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')


