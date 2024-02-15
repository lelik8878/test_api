from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def get_articles_list(request):
    articles_queryset = Article.objects.all()
    serializer = ArticleSerializer(articles_queryset, many=True)
    return Response(serializer.data)
