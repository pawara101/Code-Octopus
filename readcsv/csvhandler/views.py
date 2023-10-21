import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class CSVItemView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            with open('C:/Users/USER/OneDrive/Python3/django/Octopus Task/Code/data1.csv', 'r') as file:
                reader = csv.DictReader(file)
                items = [item for item in reader]

            serialized_items = []
            for item_data in items:
                item = Item(**item_data)
                serialized_items.append(ItemSerializer(item).data)

            return Response(serialized_items, status=status.HTTP_200_OK)

        except FileNotFoundError:
            return Response({'message': 'CSV file not found.'}, status=status.HTTP_404_NOT_FOUND)
