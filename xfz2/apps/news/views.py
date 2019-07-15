from django.shortcuts import render


# Create your views here.
def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request, 'news/index.html')


def news_detail(request, news_id):
    """
    新闻详情
    :param request:
    :param news_id: 接收到的news id
    :return:
    """
    print(news_id)
    return render(request, 'news/news_detail.html')


def search(request):
    """
    搜索界面
    :param request:
    :return:
    """
    return render(request, 'search/search.html')
