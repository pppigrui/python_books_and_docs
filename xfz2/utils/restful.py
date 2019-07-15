# coding=utf-8
"""
author: xiaorui
date: 2019-07-14 10:59
"""
from django.http import JsonResponse


class HttpCode(object):
    """
    状态码
    """
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500


def result(code=200, message="", data=None, kwargs=None):
    """
    返回的JsonResponse
    :param code: 状态码 默认200
    :param message:
    :param data:
    :param kwargs: 想要传递的内容, 需要dict格式
    :return:
    """
    json_dict = {"code": code, "message": message, "data": data}
    if isinstance(kwargs, dict):
        if all([kwargs, kwargs.keys()]):
            json_dict.update(kwargs)

    return JsonResponse(json_dict)


def ok():
    """
    返回成功 200
    :return:
    """
    return result()


def params_error(message="", data=None):
    """
    参数错误 400错误码
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.paramserror, message=message, data=data)


def unauth(message="", data=None):
    """
    没有权限 401
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.unauth, data=data, message=message)


def method_error(message="", data=None):
    """
    请求方法错误 405
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.methoderror, data=data, message=message)


def server_error(message="", data=None):
    """
    服务器内部错误 500
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.servererror, data=data, message=message)
