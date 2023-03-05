from django import forms
from .models import Album
# from .models import Image


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('image', 'title', 'artist', 'genre')


# class ImageForm(forms.ModelForm):

#     class Meta:
#         model = Image
#         fields = ()
