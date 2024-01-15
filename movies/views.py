from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(typ='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(typ='comedy')
    serializer_class = MovieSerializer
