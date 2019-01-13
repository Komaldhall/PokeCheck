from django.shortcuts import render, redirect
from .models import *
import requests
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'its_pokemon/index.html')
def gen1(request):
    return render(request, 'its_pokemon/generation-i.html')
def gen2(request):
    return render(request, 'its_pokemon/generation-ii.html')

def gen3(request):
    return render(request, 'its_pokemon/generation-iii.html')
def gen4(request):
    return render(request, 'its_pokemon/generation-iv.html')
def gen5(request):
    return render(request, 'its_pokemon/generation-v.html')

def gen6(request):
    return render(request, 'its_pokemon/generation-vi.html')
def gen7(request):
    return render(request, 'its_pokemon/sun-moon.html')
def check(request):
    if request.method == 'POST':
        display=0
        form=request.POST
        errors = []
        if len(form['pokecheck'])>3 or int(form['pokecheck'])<1:
            errors.append("Pokemon Id doesn't exist")
        
            if errors:
                for e in errors:
                    messages.error(request, e)
                    print('inerror')
                    
                    return render(request, 'its_pokemon/index.html')
        else:
            print(form['pokecheck'])
            print('https://pokeapi.co/api/v2/pokemon/'+form['pokecheck']+'/')
            response1 = requests.get('https://pokeapi.co/api/v2/pokemon/'+form['pokecheck']+'/')
            data1 = response1.json()
            
            url=data1['species']['url']
            response2 = requests.get(url)
            data2 = response2.json()
            display=1
            context={
                'name':data1['name'],
                'id':data1['id'],
                'weight':data1['weight'],
                'height':data1['height'],
                'generation':data2['generation']['name'],
                'growth_rate':data2['growth_rate']['name'],
                # 'habitat':data2['habitat']['name'],
                'display':display
            }
            return render(request, 'its_pokemon/index.html', context)
                
    return render(request, 'its_pokemon/index.html')
