from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.


def content(request):
    article = Article.objects.all()[0]
    id = article.article_id
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.publish_date
    return_str = 'id : %s , title : %s , brief_content : %s , content : %s , publish_date : %s' % (
        id, title, brief_content, content, publish_date)

    return HttpResponse(return_str)
