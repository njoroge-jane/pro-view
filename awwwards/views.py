from pyexpat import model
from re import U
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm,ProfileForm
from .models import Post,Profile
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, PostSerializer

# Create your views here.


def index(request):
  posts = Post.objects.all()
  current_user = request.user

  return render(request,'index.html', {"posts": posts}, {"current_user": user})

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
        return redirect('home')

    else:
        form = PostForm()
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
class PostList(APIView):
    def get(self,request, format = None):
        all_post = Post.objects.all()
        serializer = PostSerializer(all_post, many = True)
        return Response(serializer.data)

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializer = ProfileSerializer(all_profiles, many = True)
        return Response(serializer.data)