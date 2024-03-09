from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from quotes.models import Quote
from .serializers import QuoteSerializer

# Create your views here.


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        author = serializer.validated_data.get("author")
        hide_creator = serializer.validated_data.get("hide_creator")
        serializer.save(creator=self.request.user)


class QuoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    lookup_field = "pk"


class QuoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


class QuoteDestroyAPIView(generics.DestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUser]
    lookup_fields = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
