from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie
# Create your views here.
def index(request):
    return render(request,'index.html')

def addmovie(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index(request)
    return render(request,'addmovie.html',{'form':form})

def listmovies(request):
    movies_list=Movie.objects.all()
    return render(request,'listmovies.html',{'movies_list':movies_list})
