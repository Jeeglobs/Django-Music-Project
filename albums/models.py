from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    # CHOICES = (
    #     ('Bluegrass', 'Bluegrass'),
    #     ('Classical', 'Classical'),
    #     ('Country', 'Country'),
    #     ('Electronic', 'Electronic'),
    #     ('Hip Hop', 'Hip Hop'),
    #     ('Jazz', 'Jazz'),
    #     ('Metal', 'Metal'),
    #     ('Pop', 'Pop'),
    #     ('Rock', 'Rock'),
    # )
    # genre = models.ChoiceField(choices=CHOICES)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
        # without this, each album will be displayed only as an object
