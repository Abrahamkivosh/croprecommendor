from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from recommendor.modules.analytic import CropRecommendor

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
    return render(request, "index.html", {"crop": results,'time': datetime.today().year()})
