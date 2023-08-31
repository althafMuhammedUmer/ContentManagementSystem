from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category, blank=True)
    
    def validate_pdf_extension(document):
        if not document.name.lower().endswith('.pdf'):
            raise ValidationError("Only PDF documents are allowed.")
        
    document = models.FileField(upload_to='content-documents/', validators=[validate_pdf_extension] )

    def __str__(self):
        return self.title




    
    

    
