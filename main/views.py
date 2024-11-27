from django.shortcuts import render,redirect
import requests

# Create your views here.

def translate_view(request):
    if request.method == "POST":
        tekst = request.POST.get("text")
        source_language = request.POST.get("source_language")
        target_language = request.POST.get("target_language")

        url = "https://google-translator9.p.rapidapi.com/v2"
        
        payload = {
            "q": f"{tekst}",
            "source": f"{source_language}",
            "target": f"{target_language}",
            "format": "text"
        }
        headers = {
            "x-rapidapi-key": "43efd24fbamsh1736462130f8905p1daa18jsn85847d18e85a",
            "x-rapidapi-host": "google-translator9.p.rapidapi.com",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        translated_text = response.json()['data']['translations'][0]['translatedText']
        
        context = {
            "translated_text": translated_text
        }

        return render(request, 'index.html', context)
    else:        
        return render(request, 'index.html')