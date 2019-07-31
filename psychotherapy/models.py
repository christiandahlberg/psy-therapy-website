from django.db import models
from django.core.validators import RegexValidator

# 'Om psykodynamisk psykoterapi'
class About(models.Model):
    """ Edits the 'About' section to whatever """
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.title

# 'Priser och kontakt'
class Prices(models.Model):
    """ Edits the 'Prices' section to whatever """
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    address = models.CharField(max_length=100)
    tram = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    phone_regex = RegexValidator(regex=r'^([+]46)(7[0236])\s?-?\s?(\d{4})\s?(\d{3})$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    
    class Meta:
        verbose_name_plural = "Prices"

    def __str__(self):
        return self.title

class Frontpage(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Frontpage"

    def __str__(self):
        return self.title