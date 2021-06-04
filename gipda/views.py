from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def grammar(request):
    return render(request,'grammar.html')
def contents(request):
    return render(request,'contents.html')
def subject(request):
    return render(request,'subject.html')