from django import forms

from .models import Mesto

class MestoForm(forms.Form):
    jmeno = forms.CharField()
    zeme = forms.CharField()
    zajimavost = forms.CharField()
    pocet_obyvatel = forms.IntegerField(label="Počet obyvatel")
    hlavni_mesto = forms.BooleanField(label="Hlavní město", required=False)

class MestoModelForm(forms.ModelForm):
    class Meta:
        model = Mesto
        fields = "__all__"

        labels = {
            "zeme": "Ve které zemi toto msto leží",
            "zajimavost": "Napiš zajímavé informace o dané zemi"
        }