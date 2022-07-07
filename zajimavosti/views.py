from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
# tohle jsou view funkce

mesta = {
    "Praha": "V Praze jsou Hradčany.",
    "Brno": "V Brně je Bar, který neexistuje.",
    "Ostrava": "V Ostravě je Stodolní.",
    "Liberec": "Liberec má hezkou zoo.y"
}

def index(request):
    return HttpResponse("<h1>Tohle je hlavní stránky projektu.</h1>")

def pocasi(request):
    return HttpResponse("<p>Dnes bude hezky.</p>")

def doprava(request):
    return HttpResponse("<p>Všechny ulice jsou prázdné, všichni jsou u vody.</p>")

def detail(request, mesto):
    mesto = mesto.lower().capitalize()
    if mesto in mesta.keys():
        info = mesta[mesto]
        response = f"<p>Tohle jsou informace o městě {mesto}.</p>"
        response += f"<p>{info}</p>"
        return HttpResponse(response)
    else:
        raise Http404("Dané město v naší aplikaci neexistuje.")

def seznam(request):
    response = "<h1>Seznam všech měst</h1>"
    response += "<ul>"
    for mesto in mesta:
        response += f"<li>{mesto}</li>"
    response += "</ul>"
    return HttpResponse(response)
