from django.db.models import query
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .serializers import FileUploadedSerializer
from accounts.permissions import IsSenderOrReadOnlyView
from .models import Uploader
from rest_framework.response import Response
from django.db.models.query import Q



# Create your views here.
class FileDownloadUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileUploadedSerializer
    permission_classes = (IsSenderOrReadOnlyView,)
    queryset = Uploader.objects.all()
    lookup_field = 'file_code'


class FileDownloadConfirmation(APIView):
    def get(self, request, file_code):
        try:
            file_dl = Uploader.objects.get(file_code=file_code)
            return Response(data={'file': file_dl}, status=200)
        except Uploader.DoesNotExist:
            return Response(data={'file': 'file object not found'}, status=404)


class FilesUploadedListApiView(generics.ListAPIView):
    serializer_class = FileUploadedSerializer
    permission_classes = (IsSenderOrReadOnlyView,)
    queryset = Uploader.objects.all()


class FileUploadedSearchListApiView(generics.ListAPIView):
    serializer_class = FileUploadedSerializer
    permission_classes = (IsSenderOrReadOnlyView,)

    def get_queryset(self):
        query = self.request.GET.get("query")
        return Uploader.objects.filter(Q(title__icontains=query) | 
                                        Q(file_code=query) | 
                                        Q(sender__icontains=query)
            )


class FileUploadFormApiView(generics.CreateAPIView):
    serializer_class = FileUploadedSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    