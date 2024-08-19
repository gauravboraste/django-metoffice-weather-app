from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from django import forms
import requests
from .models import ClimateData
from .serializers import ClimateDataSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import ClimateDataForm

def gaurav(request):
    return render(request, 'data.html')
# class ClimateDataForm(forms.Form):
#     region = forms.CharField(label='Region', max_length=100)
#     parameter = forms.CharField(label='Parameter', max_length=100)
# @csrf_exempt
# def fetch(request):
#     if request.method == 'POST':
#         form = ClimateDataForm(request.POST)
#         if form.is_valid():
#             region = form.cleaned_data['region']
#             parameter = form.cleaned_data['parameter']

#             url = f'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt'
#             response = requests.get(url)

#             if response.status_code == 200:
#                 data = response.text
#                 lines = data.splitlines()

#                 # Skip the first 5 lines, which might be headers or metadata
#                 for line in lines[5:]:
#                     if not line.strip():
#                         continue  # Skip empty lines

#                     values = line.split()

#                     if len(values) < 13:  # Assuming we expect at least 13 columns (year + 12 months)
#                         continue  # Skip lines that don't have enough columns

#                     try:
#                         year = int(values[0])  # Convert the first value to an integer (the year)
#                     except ValueError:
#                         continue  # Skip the line if the year conversion fails

#                     # Now process the monthly data
#                     for i, month in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
#                         try:
#                             value = float(values[i + 1])  # Monthly values start from index 1
#                         except (ValueError, IndexError):
#                             value = None  # Handle cases where the value might be missing or invalid

#                         if value is not None:
#                             serializer = ClimateDataSerializer(data={
#                                 'year': year,
#                                 'month': month,
#                                 'value': value,
#                                 'parameter': parameter,
#                                 'region': region,
#                             })

#                             if serializer.is_valid():
#                                 serializer.save()
#                             else:
#                                 print(serializer.errors)  # Log errors for debugging

#                 return JsonResponse({'status': 'Data successfully stored in the database.'})
#             else:
#                 return JsonResponse({'error': 'Failed to retrieve data'}, status=400)
#     else:
#         form = ClimateDataForm()

#     return render(request, 'form.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def fetch(request):
    if request.method == 'POST':
        form = ClimateDataForm(request.POST)
        if form.is_valid():
            region = form.cleaned_data['region']
            parameter = form.cleaned_data['parameter']

            url = f'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.text
                lines = data.splitlines()

                # Skip the first 5 lines, which might be headers or metadata
                for line in lines[5:]:
                    if not line.strip():
                        continue  # Skip empty lines

                    values = line.split()

                    if len(values) < 13:  # Assuming we expect at least 13 columns (year + 12 months)
                        continue  # Skip lines that don't have enough columns

                    try:
                        year = int(values[0])  # Convert the first value to an integer (the year)
                    except ValueError:
                        continue  # Skip the line if the year conversion fails

                    # Now process the monthly data
                    for i, month in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                        try:
                            value = float(values[i + 1])  # Monthly values start from index 1
                        except (ValueError, IndexError):
                            value = None  # Handle cases where the value might be missing or invalid

                        if value is not None:
                            serializer = ClimateDataSerializer(data={
                                'year': year,
                                'month': month,
                                'value': value,
                                'parameter': parameter,
                                'region': region,
                            })

                            if serializer.is_valid():
                                serializer.save()
                            else:
                                print(serializer.errors)  # Log errors for debugging

                return JsonResponse({'status': 'Data successfully stored in the database.'})
            else:
                return JsonResponse({'error': 'Failed to retrieve data'}, status=400)
    else:
        form = ClimateDataForm()

    return render(request, 'form.html', {'form': form})


  
# def get_data(request):
#     region = request.GET.get('region')
#     parameter = request.GET.get('parameter')
#     year = request.GET.get('year')
#     month = request.GET.get('month')

#     # Retrieve unique values for each attribute
#     years = ClimateData.objects.values_list('year', flat=True).distinct()
#     months = ClimateData.objects.values_list('month', flat=True).distinct()
#     parameters = ClimateData.objects.values_list('parameter', flat=True).distinct()

#     # Filter the data based on the selected attributes
#     data = ClimateData.objects.filter(region=region, parameter=parameter, month=month)

#     serializer = ClimateDataSerializer(list(data), many=True)

#     # Generate the chart data
#     chart_data = []
#     for item in serializer.data:
#         chart_data.append({'label': item['year'], 'y': item['value']})

#     return render(request, 'display.html', {
#         'data': serializer.data,
#         'chart_data': chart_data,
#         'years': years,
#         'months': months,
#         'parameters': parameters,
#     })

  
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import ClimateData
from .serializers import ClimateDataSerializer

def get_data(request):
    # Retrieve parameters from the GET request
    region = request.GET.get('region')
    parameter = request.GET.get('parameter')
    year = request.GET.get('year')

    # Retrieve unique values for each attribute
    regions = ClimateData.objects.values_list('region', flat=True).distinct().order_by('region')
    years = ClimateData.objects.values_list('year', flat=True).distinct().order_by('year')
    parameters = ClimateData.objects.values_list('parameter', flat=True).distinct()

    # Filter the data based on the selected attributes
    data = ClimateData.objects.all()
    if region:
        data = data.filter(region=region)
    if parameter:
        data = data.filter(parameter=parameter)
    if year:
        data = data.filter(year=year)

    # Sort data by month (assuming month field contains strings like "Jan", "Feb", etc.)
    data = data.order_by('month')

    serializer = ClimateDataSerializer(data, many=True)

    # Generate the chart using Matplotlib
    fig, ax = plt.subplots()
    months = [item['month'] for item in serializer.data]
    values = [item['value'] for item in serializer.data]
    
    ax.plot(months, values, marker='o')
    ax.set_title(f'Climate Data for {year}-{parameter}')
    ax.set_xlabel('Month')
    ax.set_ylabel(f'{parameter}')

    # Save the plot to a BytesIO object and encode it as a base64 string
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Pass the base64 image to the template
    return render(request, 'display.html', {
      'regions': regions,
      'years': years,
      'parameters': parameters,
      'plot_url': f"data:image/png;base64,{image_base64}"
  })


