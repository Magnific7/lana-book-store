from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = 'books'

    image = models.ImageField(upload_to='books/', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

