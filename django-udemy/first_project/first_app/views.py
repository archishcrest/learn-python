from django.shortcuts import render
from django.http import HttpResponse
from . import form

from first_app.models import Topic, WebPages, AccessRecord
# Create your views here.


def index(request):

	webpages_list = AccessRecord.objects.order_by('date')
	my_dist = {
		'insert_me': 'Hello World Template'
	}
	data_dict = {
		'access_record': webpages_list,
		'insert_me': 'Hello World Template'
	}
	return render(request,"first_app/index.html",context=data_dict)



def form_name_view(request):
    forms = form.FormName()

    if request.method == 'POST':
    	forms = form.FormName(request.POST)

    if request.method == 'POST':
        forms = form.FormName(request.POST)

        if forms.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+forms.cleaned_data['name'])
            print("EMAIL: "+forms.cleaned_data['email'])
            print("TEXT: "+forms.cleaned_data['text'])

    return render(request,'first_app/forms.html',{'form':forms})
