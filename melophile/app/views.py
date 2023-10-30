from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Broadcast, AudioFile


from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,View
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.db.models.query import QuerySet,Q 
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView, LogoutView

from .models import AudioFile, Broadcast, Playlist, Song,Uploadsong
from .models import Uploadsong

# Create your views here.

class User_Creation(FormView):
    template_name='registrationform.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(User_Creation, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(User_Creation, self).get(*args, **kwargs)
      
    

class CustomLoginView(LoginView):
    template_name='login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')    

def LandingPageView(request):
    return render(request, 'landing.html')
    
class Home(ListView):
    model= Song
    template_name='home.html'
    success_url=reverse_lazy('landing')
    

class ShowAll(ListView):
    model=Song
    context_object_name='home'
    template_name='show.html'
    success_url=reverse_lazy('home')
    
class SearchViewsong(ListView):
    model=Song
    template_name='searchsong.html'
    
    success_url=reverse_lazy('showall')

    def get_queryset(self):
        query = self.request.GET.get('q')  
        if query:
            
            return Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))
        else:
            
            return Song.objects.none()

class SongDetailView(DetailView):
    model=Song
    context_object_name = 'song'
    template_name='direct_detail.html'


@login_required(login_url='login/') 
def add_to_playlist(request, song_id):
    user = request.user
    
    
    playlist, created = Playlist.objects.get_or_create(user=user)

    
    song = get_object_or_404(Song, pk=song_id)

    
    if song not in playlist.songs.all():
        playlist.songs.add(song)

        return redirect('showplaylist')
    else:
        return redirect('showplaylist')




class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist.html'
    context_object_name = 'playlists'

    def get_queryset(self):
        
        user = self.request.user
        return Playlist.objects.filter(user=user).prefetch_related('songs')

            
class Uploadsong(LoginRequiredMixin, CreateView):
    model = Uploadsong
    template_name = 'songupload.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form ):
        form.instance.user=self.request.user
        return super().form_valid(form)

# class PodcastCreateView(LoginRequiredMixin, CreateView):
#     model = AudioFile 
#     fields=['user','title','audio_file']
#     template_name = 'podcast_create.html' 
#     success_url = reverse_lazy('home')  

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

class Createtitle(CreateView):
    model=Broadcast
    template_name='title.html'
    fields=['cover','title']
    success_url=reverse_lazy('addpod')
    def form_valid(self, form ):
        form.instance.user=self.request.user
        return super().form_valid(form)
    


class uploadtoexisting(CreateView):
    model=AudioFile
    template_name='pod.html'
    fields='__all__'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    





# class CreateInstanceView(View):
#     template_name = 'mech.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         # Access the input values from the form
#         mood1 = request.POST.get('mood1', '')
#         mood2 = request.POST.get('mood2', '')
#         mood3 = request.POST.get('mood3', '')

#         # Check if any mood input is empty

class seepod(ListView):
    model=Broadcast
    template_name='podcast_view.html'
    success_url=reverse_lazy('podcast')




class AudioListView(ListView):
    template_name = 'audio_list.html'
    context_object_name = 'audio_files'

    def get_queryset(self):
        title = self.kwargs['title']
        broadcast = get_object_or_404(Broadcast, title=title)
        return AudioFile.objects.filter(broadcast=broadcast)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs['title']
        context['broadcast'] = get_object_or_404(Broadcast, title=title)
        return context

class podDetailView(DetailView):
    model=AudioFile
    template_name='poddetail.html'
    success_url=reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class UserUploadListView(ListView):
    template_name = 'songyour.html'
    model = Uploadsong
    context_object_name = 'uploadsongs'

    def get_queryset(self):
        return Uploadsong.objects.filter(user=self.request.user)