from rest_framework import generics
from .models import Banner
from .serializers import BannerSerializer


class BannerListAPIView(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.filter(is_active=True).order_by('order', '-created_at')
