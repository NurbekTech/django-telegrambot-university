from rest_framework.generics import ListAPIView
from .models import Menu
from .serializers import MenuSerializer


class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.all().order_by("order")
    serializer_class = MenuSerializer
