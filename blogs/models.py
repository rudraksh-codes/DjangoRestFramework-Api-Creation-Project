from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField() 

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment = models.TextField(max_length=100)  
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment
