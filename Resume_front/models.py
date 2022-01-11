from django.db import models

class msgreq(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    msg = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name