from django.db import models


class Upload(models.Model):
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc
    

class UploadFile(models.Model):
    file = models.FileField(upload_to="Files")
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc