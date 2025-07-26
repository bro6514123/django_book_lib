from django.db import models
from django.urls import reverse


class Ganre(models.Model):
    name = models.CharField(max_length=63, db_index=True)
    slug = models.SlugField(max_length=63, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ganre'
        verbose_name_plural = 'Ganres'

    def __str__(self):
        return self.name

class Author(models.Model):
    fullname = models.CharField(max_length=63, db_index=True)
    slug = models.SlugField(max_length=63, unique=True)

    class Meta:
        ordering = ('fullname',)
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("main:author", args=[self.slug])

class Book(models.Model):
    ganres = models.ManyToManyField(Ganre, related_name='books')
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=63)
    photo = models.ImageField(upload_to='books/posters/', blank=True)
    desk = models.CharField(max_length=127, blank=True)
    file = models.FileField(upload_to='books/pdfs/')

    def get_absolute_url(self):
        return reverse("main:details_of_book", args=[self.id])