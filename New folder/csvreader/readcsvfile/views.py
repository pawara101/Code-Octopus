import csv
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item  # Import your Item model
from .serializers import ItemSerializer  # Import your ItemSerializer

class CSVItemView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            csv_file_path = 'C:/Users/USER/OneDrive/Python3/django/Octopus Task/Code/data2.csv'

            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = []

                # Assuming your CSV columns match your Item model fields
                for row in reader:
                    data.append(row)

            # Serialize the data using your ItemSerializer
            serializer = ItemSerializer(data=data, many=True)

            # Check if the data is valid and return it as JSON
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                # Log or print serializer.errors to identify the specific issue
                print(serializer.errors)
                return Response({'message': 'Data serialization error.'}, status=status.HTTP_400_BAD_REQUEST)

        except FileNotFoundError:
            return Response({'message': 'CSV file not found.'}, status=status.HTTP_404_NOT_FOUND)
