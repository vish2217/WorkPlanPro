from django.db import models
class Position (models.Model):
   title=models.CharField(max_length=50)

class Task(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     due_date = models.DateField()
    
     def __str__(self):
      return self.title

class CustomerMessage(models.Model):
   name=models.CharField(max_length=100)
   email=models.EmailField()
   message=models.TextField()
   submitted_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return f"Message from{self.name}"
