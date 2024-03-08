from django.db import models

class Scraper(models.Model):
    url = models.CharField(max_length=255)
    target = models.CharField(max_length=255)