from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=200, verbose_name="blog title", unique=True, null=True)
    description=models.TextField()
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    thumbnail=models.ImageField(upload_to="thumbnails", default="default.jpg")
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts")