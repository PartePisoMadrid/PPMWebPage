from django.db import models
from django.urls import reverse

# Create your models here.
class Parte(models.Model):
	title        = models.CharField(max_length=70)
	shareMessage = models.TextField(blank=True, null=True)
	idGSheet     = models.CharField(max_length=270, blank=True, null=True)
	shared       = models.BooleanField(default=True)

	def get_absolute_url(self):

	    return reverse("parte-detail", kwargs={"id":self.id})