from django.db import models
from .utils import code_generator,create_shortcode
from .validators import validate_url
from django.core.validators import URLValidator

class shortner_class(models.Model):
    url = models.CharField(max_length=200,validators = [validate_url])
    shortcode = models.CharField(max_length=15, unique = True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.url)
    

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode =="":
            self.shortcode = create_shortcode(self)
        super(shortner_class,self).save(*args,**kwargs)
    
    def get_short_url(self):
        return "http://127.0.0.1:8000/urlshortner/{shortcode}".format(shortcode = self.shortcode)