from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    # goes to the DB and gets all instances of the model Album (Django ORM) = query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary {'albums... etc}


def add_album(request):
    if request.method == 'POST':
        new_album = AlbumForm(request.POST)
        if new_album.is_valid():
            new_album.save()
            return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})

# click on album on homepage -> get_info -> go to page with info
# -> have links on this page to edit album, delete album, and go back to homepage


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        new_album = AlbumForm(request.POST, instance=album)
        if new_album.is_valid():
            new_album.save()
            return redirect('home')
    form = AlbumForm(instance=album)
    return render(request, 'albums/edit_album.html', {'form': form, 'pk': pk})


def delete_album(request):
    # remove album from DB and save
    # GET & POST
    pass


def get_info(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/get_info.html', {'album': album})
