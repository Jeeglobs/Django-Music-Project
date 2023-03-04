from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    # CHOICES = (
    #     ('Pop', 'Pop'),
    #     ('Rock', 'Rock'),
    #     ('Metal', 'Metal'),
    #     ('Hip Hop', 'Hip Hop'),
    #     ('Classical', 'Classical'),
    #     ('Country', 'Country'),
    #     ('Bluegrass', 'Bluegrass'),
    #     ('Jazz', 'Jazz'),
    #     ('Electronic', 'Electronic'),
    # )
    # genre = models.ChoiceField(choices=CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
        # without this, each album will be displayed only as an object
