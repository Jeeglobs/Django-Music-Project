from django.shortcuts import render
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    # goes to the DB and gets all instances of the model Album (Django ORM) = query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary {'albums... etc}


def add_album(request):
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})

# click on album on homepage -> get_info -> go to page with info
# -> have links on this page to edit album, delete album, and go back to homepage


def edit_album(request):
    # update existing album and save
    # GET & POST
    pass


def delete_album(request):
    # remove album from DB and save
    # GET & POST
    pass


def get_info(request):
    # see all information--title, artist, date_created, etc.
    # GET
    pass
