from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
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


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    all_articles = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:5]
    paginator = Paginator(all_articles, 6)

    num_pages = paginator.num_pages
    print(num_pages)
    next_page = 2
    previous_page = 1
    if page >= num_pages:
        page = num_pages
        next_page = page
        previous_page = page - 1
    elif page <= 1:
        page = 1
        next_page = page + 1
        previous_page = page
    else:
        next_page = page + 1
        previous_page = page - 1

    curr_page_articles = paginator.page(page)

    return render(request, 'index.html', {
        'article_list':  curr_page_articles,
        'num_pages': range(1, num_pages + 1),
        'next_page': next_page,
        'previous_page': previous_page,
        'top5_article_list': top5_article_list,
    })


def get_detail_page(request, article_id):
    articles = Article.objects.all()
    curr_article = None
    previous_article = None
    next_article = None

    previous_index = 0
    next_index = 0
    for index, article in enumerate(articles):
        if index == 0:
            previous_index = index
            next_index = index + 1
        elif index == len(articles) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            break

    previous_article = articles[previous_index]
    next_article = articles[next_index]
    section_list = curr_article.content.split('\n')
    return render(request, 'detail.html', {
        'title': curr_article.title,
        'section_list': section_list,
        'previous_article_id': previous_article.article_id,
        'previous_article_title': previous_article.title,
        'next_article_id': next_article.article_id,
        'next_article_title': next_article.title,
    })
