from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serialazer = ItemSerializer(items, many=True)
    return Response(serialazer.data)

@api_view(['POST'])
def addItem(request):
    serialazer = ItemSerializer(data=request.data)
    if serialazer.is_valid():
        serialazer.save()

    return Response(serialazer.data)