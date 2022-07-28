from django.http import Http404
from django.shortcuts import get_object_or_404, render

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
    mesta = Mesto.objects.all().order_by("-pocet_obyvatel")
    return render(request, "zajimavosti/index.html", {
        "mesta": mesta
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
    try:
        mesto = Mesto.objects.get(jmeno=mesto)
    except Mesto.DoesNotExist:
        raise Http404("Dané město v naší aplikaci neexistuje.")
    # mesto = get_object_or_404(Mesto, jmeno=mesto)
    return render(request, "zajimavosti/detail.html", {
        "mesto": mesto,
     })
    

def seznam(request):
    mesta = Mesto.objects.all().order_by("-jmeno")
    return render(request, "zajimavosti/seznam.html", {
        "mesta": mesta
    })
