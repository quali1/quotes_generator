from rest_framework import serializers
from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    creator = serializers.CharField(read_only=True)
    hide_creator = serializers.BooleanField()
    likes_count = serializers.IntegerField(read_only=True)
    created = serializers.CharField

    class Meta:
        model = Quote
        fields = [
            "id",
            "title",
            "author",
            "creator",
            "hide_creator",
            "likes_count",
            "created",
        ]
