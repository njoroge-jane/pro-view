from pyexpat import model
from re import U
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm,ProfileForm
from .models import Image,Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
  images = Image.objects.all()


  return render(request,'index.html', {"images": images})


def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
        return redirect('home')

    else:
        form = UploadImageForm()
    return render(request, 'new_upload.html', {"form": form})
  
def profile(request):
  current_user = request.user
  if request.method == 'POST':

    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
          profile = form.save(commit=False)
          profile.user = current_user
          profile.save()

  else:
        form = ProfileForm()        
  return render(request, 'profile.html',{"form":form})



def search_results(request):

    if 'users' in request.GET and request.GET["users"]:
        search_term = request.GET.get("users")
        searched_users = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
