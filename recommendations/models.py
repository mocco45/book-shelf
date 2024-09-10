from django.db import models
from accounts.models import CustomUser
from books.models import books

class recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    recommended_at = models.DateTimeField()
    
    def __str__(self):
        return f'recommendation for {self.user} - {self.book}'

