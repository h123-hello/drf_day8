from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Computer

from app.filter import LimitFilter, ComputerFilterSet
from app.paginations import MyCoursePagination
from app.serializers import ComputerModelSerializer
from utils.response import APIResponse
from app.filter import LimitFilter, ComputerFilterSet


# Create your views here.
class ComputerListAPIGView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # 通过此参数配置过滤的器类
    filter_backends = [SearchFilter, OrderingFilter, LimitFilter, DjangoFilterBackend]

    # 指定当前搜索条件
    search_fields = ["name", "price"]
    # 指定排序的条件
    ordering = ["price"]

    filter_class = ComputerFilterSet
