from django.shortcuts import render


# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html')


def star(request):
    return render(request, 'star2.html')
