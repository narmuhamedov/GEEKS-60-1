from django.db import models


class Blog(models.Model):
    name_blog = models.CharField(max_length=100, verbose_name='enter your name blog')
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    TYPE_BLOG = (
        ("Education", "Education"),
        ("Travel", "Travel")
    )
    type_blog = models.CharField(max_length=100, choices=TYPE_BLOG, default="Education")
    url_blog = models.URLField(verbose_name='Enter your link', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_blog
    

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    # FileField, IntegerField, PostiveIntergerField, URLField - на дом самостоятельно
    # Изучить дома атрибуты - null, verbose_name, blank, 
    # class Meta - изучить дома что делает данный класс


class Reviews(models.Model):
    #related_name - он аналог контекстного ключа - когда мы хотим получить все комменты к какому то объекту мы обращаемся к related_name
    choice_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="review")
    MARKS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟")
    )
    marks =  models.CharField(max_length=100, choices=MARKS, default="🌟🌟🌟🌟")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.choice_blog} : {self.marks}'
    

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'