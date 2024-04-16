from django.shortcuts import render, redirect
from . import models
from datetime import datetime

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows' : models.display_shows()
    }
    return render(request, 'shows.html', context)

#add show to db
def new_show(request):
    return render(request, 'add_show.html')

#submit show to db
def submit_show(request):
    print(request.method)
    if request.method == 'POST':
        models.Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], description = request.POST['description'])
    return render(request, 'read.html')

#display show
def display_show(request, show_id):
    context = {
        'show': models.Show.objects.get(id = show_id),
    }
    return render(request, 'shows/editshow.html', context)
# Create your views here.
