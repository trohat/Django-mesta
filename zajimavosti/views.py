from django.http import Http404
from django.shortcuts import render

from .models import Mesto

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
    jmeno = mesto.lower().capitalize()
    try:
        mesto = Mesto.objects.get(jmeno=jmeno)
        return render(request, "zajimavosti/detail.html", {
            "mesto": mesto.jmeno,
            "popis": mesto.zajimavost
        })
    except:
        raise Http404("Dané město v naší aplikaci neexistuje.")

def seznam(request):
    mesta = Mesto.objects.all().order_by("-jmeno")
    return render(request, "zajimavosti/seznam.html", {
        "mesta": mesta
    })
