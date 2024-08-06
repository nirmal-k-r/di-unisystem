from django.db import models

# Create your models here.
class Courses(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    # code=models.CharField(max_length=10)
    # description=models.TextField()
    # credits=models.IntegerField()
    # department=models.CharField(max_length=100)
    # level=models.IntegerField()
    # semester=models.IntegerField()
    year=models.IntegerField()
    def __str__(self):
        return self.name