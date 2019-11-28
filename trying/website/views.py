from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.http import HttpResponse
from .forms import RoastForm
from .models import Roast
from random import random
# Create your views here.
def index(request):
    latest_question_list = Roast.objects.order_by('-pub_date')
    R= random()*254
    G=random()*254
    B=random()*254
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoastForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            roast_Text = form.cleaned_data['roast']
            Roast(roast_text=roast_Text,pub_date=timezone.now()).save()

            return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RoastForm()
    context = {
        'q': latest_question_list,
        'form':form,
        'r':R,
        'g':G,
        "b":B
    }
    return render(request,'index.html',context)
