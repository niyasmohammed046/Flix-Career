from django.db import models
from django.utils.text import slugify


class Skills(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city



Job_type_choices = [
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Internship','Internship')
    
]
class JobPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,max_length=40,unique=True)
    desc = models.TextField()
    salary = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    location = models.OneToOneField(Location,null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, on_delete = models.CASCADE)
    skills = models.ManyToManyField(Skills,null=True)
    type = models.CharField(max_length=50,null=False,choices=Job_type_choices)

    #this is for creating slugs
    def save(self, *args, **kwargs):   
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

