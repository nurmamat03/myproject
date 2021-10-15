from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='static_image')


class Portfolio(models.Model):
    img = models.ImageField(upload_to='PORTFOLIO')
