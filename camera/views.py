from django.shortcuts import render

# Create your views here.
def camera(request):
    return render(request, 'cameraprofile.html')