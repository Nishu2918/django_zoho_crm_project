from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Unknown")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True, null=True)
    lead_id = models.CharField(max_length=100, unique=True, default="temp-lead-id")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
