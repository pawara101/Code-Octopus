import csv
import json
from django.http import JsonResponse

def CSVItemView(request,i=10):
    # Specify the path to your CSV file
    csv_file_path = 'C:/Users/USER/OneDrive/Python3/django/Octopus Task/Code/data1.csv'

    data = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    # Send JSON data as a response
    return JsonResponse(data, safe=False)
