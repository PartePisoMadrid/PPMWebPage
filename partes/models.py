from django.db import models
from django.urls import reverse

import datetime
def get_parte_name(next=True):
	monthsList = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
	getName = lambda d, m : f"Semana {d} de {m}"
	today = datetime.date.today()
	if (next):
		nextMonday = today + datetime.timedelta(7-today.weekday())
		return getName(nextMonday.day, monthsList[nextMonday.month])
	thisMonday = today - datetime.timedelta(today.weekday())
	return getName(thisMonday.day, monthsList[thisMonday.month])

# Create your models here.
class Parte(models.Model):
	title        = models.CharField(max_length=70, default=get_parte_name())
	shareMessage = models.TextField(blank=True, null=True)
	idGSheet     = models.CharField(max_length=270, blank=True, null=True)
	shared       = models.BooleanField(default=False)

	def get_absolute_url(self):

	    return reverse("parte-detail", kwargs={"id":self.id})