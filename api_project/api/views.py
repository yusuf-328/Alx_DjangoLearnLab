from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book 


from rest_framework.generics import ListAPIView
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer