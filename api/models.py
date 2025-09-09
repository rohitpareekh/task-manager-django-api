from django.db import models
from django.contrib.auth.models import User

# class Authentication(models.Model):
#     id = models.AutoField(primary_key=True)
#     email = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=128)  # hashed password

#     def save(self, *args, **kwargs):
#         # Hash password before saving
#         if not self.password.startswith("pbkdf2_"):  # avoid rehash
#             self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.email
    
#Task Model
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title