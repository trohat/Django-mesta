from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
# tohle jsou view funkce

mesta = {
    "Praha": "V Praze jsou Hradčany.",
    "Brno": "V Brně je Bar, který neexistuje.",
    "Ostrava": "V Ostravě je Stodolní.",
    "Liberec": "Liberec má hezkou zoo."
}

def index(request):
    return render(request, "zajimavosti/index.html", {
        "mesta": mesta.keys()
    })

def pocasi(request):
    slovni_popis = "slunečno"
    vitr = 5
    dest = 1.0
    return render(request, "zajimavosti/pocasi.html", {
        "slovni_popis": slovni_popis,
        "sila_vetru": vitr,
        "srazky": dest,
        "sinice_ve_vode": False
    })

def doprava(request):
    prujezdnost = False
    context =  {
        "prujezdnost": prujezdnost
    }
    return render(request, "zajimavosti/doprava.html", context)

def detail(request, mesto):
    mesto = mesto.lower().capitalize()
    if mesto in mesta.keys():
        info = mesta[mesto]
        return render(request, "zajimavosti/detail.html", {
            "mesto": mesto,
            "popis": info
        })
    else:
        raise Http404("Dané město v naší aplikaci neexistuje.")

def seznam(request):
    return render(request, "zajimavosti/seznam.html", {
        "mesta": mesta
    })
