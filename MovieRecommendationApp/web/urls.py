from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/',views.detail ,name='detail'),
    path('signup/',views.signUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    # path('upload/',views.MovieBulkUploadView.as_view(),name='movies_upload')
    # spath('recommend/',views.recommend,name='recommend')
    path('upload/',views.upload_file_view,name='upload-file'),
]
