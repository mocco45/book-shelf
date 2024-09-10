from django.db import models
from accounts.models import CustomUser
from books.models import books

class reviews(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'review by {self.user} for {self.book}'
    
class rating(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    
    class Meta:
        unique_together = ('user', 'book')
    
    def __str__(self):
        return f'rating by {self.user} for {self.book})'
