from django.shortcuts import render
from .models import Podt

def post_list(request):
    posts = Podt.objects.all()
    return render(request, 'blog/post_list.html', {'Posts': posts})
# Create your views here.

