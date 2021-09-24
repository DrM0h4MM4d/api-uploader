from django.urls import path
from . import views

 
urlpatterns = [
    path('files/', views.FilesUploadedListApiView.as_view(), name='file-uploaded-list'),
    # path('file/download/confirm/', views.FileDownloadConfirmation.as_view(), name='file-download-confirm'),
    path('file/<str:code>/', views.FileDownloadUpdateDestroyApiView.as_view(), name='file-crud'),
    path('file/search/', views.FileUploadedSearchListApiView.as_view(), name='upload-search'),
    path('file/', views.FileUploadFormApiView.as_view(), name='upload')
]
