from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def movies_view(request):
    return render(request,'movies.html')

def sports_view(request):
    return render(request,'sports.html')

def politics_view(request):
    return render(request,'politics.html')
