from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField()
    url = models.URLField()
    views = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
    
    def add_view(self):
        t = Traffic(post=self)  
        t.save()
        
class Traffic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title
    
    class Meta:
        ordering = ['-date']