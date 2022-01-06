from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from recommendor.modules.analytic import CropRecommendor
# from rest_framework import views, permissions
# from recommendor.serializers import userSerializers, GroupSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

def get_time():
    time = datetime.today()
    return {'time':time}

# Create your views here.
def home_index(request):
 
    time = {
        "time": datetime.today()
    }
    
    # print(type(results))
    return render(request=request, template_name="index.html",context= time )


def form_results(request):
    data = request.POST
    nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall = (
        data["nitrogen"],
        data["phosphorus"],
        data["potassium"],
        data["temperature"],
        data["humidity"],
        data["ph"],
        data["rainfall"],
    )
    recommend = CropRecommendor(
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=potassium,
        temperature=temperature,
        humidity=humidity,
        ph=ph,
        rainfall=rainfall,
    )
    results = recommend.analyse_data()
    results = results[0]
    data = {"crop": results,
            'time': datetime.today()
            }
    return render(request, "index.html", data)

# @api_view(['GET'])
def recommend_view(request):
    data = request.GET
    # print(data.GET)
    nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall = (
        data["nitrogen"],
        data["phosphorus"],
        data["potassium"],
        data["temperature"],
        data["humidity"],
        data["ph"],
        data["rainfall"],
    )
    
    recommend = CropRecommendor(
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=potassium,
        temperature=temperature,
        humidity=humidity,
        ph=ph,
        rainfall=rainfall,
    )
    results = recommend.analyse_data()
    results = results[0]
    return JsonResponse(results, safe= False)
 