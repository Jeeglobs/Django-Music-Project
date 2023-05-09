# Generated by Django 4.1.7 on 2023-03-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_alter_album_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('alt-indie', 'Alt/Indie'), ('bluegrass', 'Bluegrass'), ('classical', 'Classical'), ('orchestral', 'Orchestral'), ('country', 'Country'), ('electronic', 'Electronic'), ('hip hop', 'Hip Hop'), ('jazz', 'Jazz'), ('metal', 'Metal'), ('pop', 'Pop'), ('punk', 'Punk'), ('reggae', 'Reggae'), ('rock', 'Rock'), ('soundtrack', 'Soundtrack')], max_length=50),
        ),
    ]
