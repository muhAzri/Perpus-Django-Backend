from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=9)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    writter = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    amount = models.IntegerField(default=0)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
