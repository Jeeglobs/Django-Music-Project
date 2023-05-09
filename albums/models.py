from django.db import models

# Create your models here.


class Album(models.Model):
    CHOICES = (
        ('alt-indie', 'Alt/Indie'),
        ('bluegrass', 'Bluegrass'),
        ('classical', 'Classical'),
        ('orchestral', 'Orchestral'),
        ('country', 'Country'),
        ('electronic', 'Electronic'),
        ('hip hop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('metal', 'Metal'),
        ('pop', 'Pop'),
        ('punk', 'Punk'),
        ('reggae', 'Reggae'),
        ('rock', 'Rock'),
        ('soundtrack', 'Soundtrack'),
    )
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(choices=CHOICES, max_length=50)

    # is upload_to '' doing anything??
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
        # without this, each album will be displayed only as an object
