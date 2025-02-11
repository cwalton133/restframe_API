from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    other_name = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="Author")
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name + " " + self.last_name
