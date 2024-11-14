from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    year=models.IntegerField()
    language=models.CharField(max_length=20)
    image=models.ImageField(upload_to="img",blank=True,null=True)

    def __str__(self):
        return self.title
