from django.urls import path

 
from . import views
from .views import  AudioListView, Createtitle, Home,  PlaylistListView, SearchViewsong, ShowAll, SongDetailView,User_Creation,CustomLoginView,CustomLogoutView,Uploadsong, UserUploadListView, podDetailView, seepod, uploadtoexisting
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPageView, name='landing'),
    path('home/', Home.as_view(), name='home'),
    path('showall/',ShowAll.as_view(),name='showall'),
    path('search/',SearchViewsong.as_view(), name='search'),
    path('register/',User_Creation.as_view(),name='register'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('detailview/<int:pk>/', SongDetailView.as_view(), name='detail'),
    path('playlist/', PlaylistListView.as_view(), name='showplaylist'),
    path('add_to_playlist/<int:song_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('addsong/',Uploadsong.as_view(),name='savesong'),
    # path('addpod/',PodcastCreateView.as_view(),name='podcastadd')
    path('title/',Createtitle.as_view(), name='title'),
    path('addpod/',uploadtoexisting.as_view(),name="addpod"),
    path('podview/',seepod.as_view(),name="seepodcast"),
    path('audio/<str:title>/',AudioListView.as_view(), name='audio_list'),
    path('audio/detail/<int:pk>/', podDetailView.as_view(), name='audio_detail'),
    path('uploadsongs/', UserUploadListView.as_view(), name='user_uploadsongs'),   
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
