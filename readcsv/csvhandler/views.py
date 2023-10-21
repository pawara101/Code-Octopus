import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class CSVItemView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            with open('C:/Users/USER/OneDrive/Python3/django/Octopus Task/Code/data2.csv', 'r') as file:
                reader = csv.DictReader(file)
                # for row in reader:
                #     Item.objects.create(id=row['id'], age=row['age'])


            data = Item.objects.all()
            serializer = ItemSerializer(data, many=True)
            return Response(serializer.data)

        except FileNotFoundError:
            return Response({'message': 'CSV file not found.'}, status=status.HTTP_404_NOT_FOUND)
