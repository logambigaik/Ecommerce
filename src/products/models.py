import os,random

from django.db import models


def get_filename_ext(filepath):
    #print(filepath)
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    #print(name, ext)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 3910209312)
    print(new_filename)
    #return new_filename
    name,ext=get_filename_ext(filename)
    print(name,ext)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    #final_filename=f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=11.10)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
