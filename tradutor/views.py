from django.shortcuts import render
from django.http import HttpResponse
from deep_translator import GoogleTranslator
# from 
# Create your views here.

def index(request):
    if request.method == "POST":
        language1 = request.POST.get('languages1')
        language2 = request.POST.get('languages2')
        text = request.POST.get('text')
        traduction = request.POST.get('traduction')

        translator = GoogleTranslator(source=language1,target=language2)
        traduction = translator.translate(text)
        tam1 = len(language1)
        tam2 = len(language2)

        context = {
            'traduction' : traduction,
            'text' : text,
            'language1' : language1,
            'language2' : language2,
            'tam1' : tam1,
            'tam2' : tam2
            }
        return render(request,'tradutor/index.html', context)
    return render(request,'tradutor/index.html' )

