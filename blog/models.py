from django.db import models


class Blog(models.Model):
    name_blog = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    TYPE_BLOG = (
        ("Education", "Education"),
        ("Travel", "Travel")
    )
    type_blog = models.CharField(max_length=100, choices=TYPE_BLOG, default="Education")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_blog

    # FileField, IntegerField, PostiveIntergerField, URLField - на дом самостоятельно
    # Изучить дома атрибуты - null, verbose_name, blank, 
    # class Meta - изучить дома что делает данный класс
    
    
