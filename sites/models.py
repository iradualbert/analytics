from django.db import models
from requests.api import get
from .utils import get_user_country


class Post(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField()
    url = models.URLField()
    views = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
    
    def add_view(self, request):
        geo_data = get_user_country(request)
        country = None
        region = None
        try:
            region = geo_data["region"]
            country = geo_data["country"]           
        except:
            pass
        t = Traffic(post=self, country=country, region=region)  
        t.save()
        
class Traffic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    country = models.TextField(max_length=100, null=True, blank=True)
    region = models.TextField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.post.title
    
    class Meta:
        ordering = ['-date']