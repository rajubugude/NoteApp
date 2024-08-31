from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Note(models.Model):

    CATEGORY = (('BUSINESS', 'Business'),
                ('PERSONAL', 'Personal'),
                ('IMPORTANT', 'Important'))

    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.CharField(max_length=15, choices=CATEGORY, default="PERSONAL")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug
            slug_base = slugify(self.title)
            slug = slug_base
            # Check if the slug is unique and modify it if necessary
            if Note.objects.filter(slug=slug).exists():
                slug = f'{slug_base}-{get_random_string(5)}'
            self.slug = slug
        super(Note, self).save(*args, **kwargs)


'''
Summary:
*args captures extra positional arguments as a tuple.
**kwargs captures extra keyword arguments as a dictionary.
In the save method, they ensure the function can accept and pass along any arguments 
required by the parent class or other function calls, allowing your model to integrate 
seamlessly with Django's ORM features.
'''