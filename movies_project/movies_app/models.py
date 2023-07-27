from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=250)
    imdb=models.IntegerField()
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.name.__str__()

