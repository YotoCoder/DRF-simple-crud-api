from rest_framework import viewsets
from rest_framework import permissions

from .models import Note
from .serializers import NoteSerializer

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializer
