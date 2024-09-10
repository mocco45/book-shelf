from django.db import models

class authors(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    biography = models.TextField(null=True, blank=True)
    
class genre(models.Model):
    name = models.CharField(max_length=255)
    
class series(models.Model):
    name = models.CharField(max_length=255, unique=True)

class books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(authors, on_delete=models.CASCADE)
    genre = models.ManyToManyField(genre)
    series = models.ForeignKey(series, on_delete=models.SET_NULL, blank=True, null=True)
    synopsis = models.TextField()
    picture = models.ImageField(upload_to='book_cover/')
    publish_date = models.DateField()
    isbn = models.CharField(max_length=255,unique=True)
    pageCount = models.IntegerField()
    
    def __str__(self):
        return self.title
 
