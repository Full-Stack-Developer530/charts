from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .serializer import *


class ChartDataAPI(APIView):
    def get(self, request):
        cache_key = 'simple_data'
        data = cache.get(cache_key)
        if not data:
            year_data = YearData.objects.prefetch_related('month_data__time_data').get(year="2024")
            serialize = CustomYearDataSerializer(year_data)
            data = [serialize.data]
            cache.set(cache_key, data, timeout=60 * 15)

        return Response(data, status=status.HTTP_200_OK)
