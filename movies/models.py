from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    director = models.ForeignKey(Person, on_delete=models.CASCADE,
                                 related_name='%(class)s_director')
    actors = models.ManyToManyField(Person, through='Role',
                                    related_name='%(class)s_actors')
    year = models.IntegerField()


class Role(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.TextField(max_length=100)
