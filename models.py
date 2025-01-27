from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    image = models.ImageField(upload_to='post_images',blank=True, null=True)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cv(models.Model):
    cv = models.FileField(upload_to ='uploads/')
    job = models.ForeignKey(Post,related_name='cv',on_delete=models.CASCADE,null=True)

class JobApplied(models.Model):
    class Meta:

        verbose_name_plural = 'Job Applies'
    status = models.CharField(max_length=255)
    job = models.ForeignKey(Post,related_name='jobApplies',on_delete=models.CASCADE)
    applied_by = models.ForeignKey(User,related_name='jobApplies',on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv,related_name="jobApplies",on_delete=models.CASCADE)


    def __str__(self):
        return self.name 




