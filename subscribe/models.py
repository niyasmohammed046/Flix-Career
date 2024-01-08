from django.db import models


news_sub = [
    ('W','Weekly'),
    ('M','Monthly')
]

class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    option = models.CharField(max_length=2,choices=news_sub)

    def __str__(self):
        return self.first_name
