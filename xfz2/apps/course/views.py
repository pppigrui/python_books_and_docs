from django.shortcuts import render


# Create your views here.

def course_index(request):
    """
    课程首页
    :param request:
    :return:
    """
    return render(request, 'course/course_index.html')


def course_detail(request, course_id):
    """
    课程详情
    :param request:
    :param course_id: 课程id
    :return:
    """
    print(course_id)
    return render(request, 'course/course_detail.html')
