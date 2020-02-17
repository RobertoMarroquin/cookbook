from django.db import models

# Create your models here.
GENRE_CHOICES = (

                 ('R', 'Rock'),
                 ('B', 'Blues'),
                 ('J', 'Jazz'),
                 ('P', 'Pop'),
                 ('Rg','Reggae')
                )

class CD(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES,null=True, blank=True)

    def __str__(self):
        return "{} by {}, {}".format(self.title, self.artist, self.date.years)
