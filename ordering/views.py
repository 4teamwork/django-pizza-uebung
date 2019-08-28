from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from ordering.models import Produkt, LieferungForm


def index(request):
    produkte = Produkt.objects.all()
    form = LieferungForm

    if request.method == 'POST':
        formset = LieferungForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponse("Bestellung gespeichert") # ToDo: Auf eigene Seite umleiten

    return render(request, "pizza/index.html", {"produkte": produkte, "form": form})
    #ToDo: zutaten ersichtlich machen

def produkt(request,id):
        produkt = get_object_or_404(Produkt,pk=id)
        return render(request, "pizza/produkt.html", {"produkt": produkt})
