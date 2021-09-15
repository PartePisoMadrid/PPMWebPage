from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ParteForm
from .models import Parte
from .utils import utils

import datetime


# Create your views here.
def parte_create_view(request, *args, **kwargs):
	parteUrl = utils.getUrlDownloadParte()
	reviseWeekDay = datetime.datetime.today().weekday()
	if reviseWeekDay==0:
		utils.createNextParte()
	if reviseWeekDay==2:
		initial_data = {
			'title': 'Semana (dd) de (mes)', 'shared':False
		}
		form = ParteForm(None, initial=initial_data)
		if request.POST:
			form = ParteForm(request.POST, initial=initial_data)
			utils.createNextParte()
			if form.is_valid():
				form.save()
				utils.shareParte(form.cleaned_data['subject'])
		context = {'form':form}
		return render(request, "partes/parte_create.html", context)
	return HttpResponseRedirect(parteUrl)

def parte_detail_view(request, id):
	context = {}
	if len(Parte.objects.all())>=id:
		obj = Parte.objects.get(id=id)
		context = {'object': obj}
	return render(request, "partes/parte_detail.html", context)