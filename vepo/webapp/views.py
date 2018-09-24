from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .forms import QuoteForm
from .painelSolar import *

def contact(request):

    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            consumo = form.cleaned_data['consumo']
            cep = form.cleaned_data['cep']


            request.session['cep'] = cep
            request.session['name'] = name
            request.session['consumo'] = consumo

            return redirect('/charts')

    else:

        form = QuoteForm()
        return render(request, 'index.html', {'form': form})


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):

        data = getPV(request.session['cep'])
        consumo = request.sessions['consumo']

        areaMedia = 10. #m2
        kitPreco = 10000. #reais
        dias = 30.
        radiacaoMedia = np.mean(data.wp.values)
        kWh = 0.8 #centavos

        radiacao = radiacaoMedia * dias * areaMedia * 0.15 * kWh
        financeiroConsumo = consumo * kWh
        economiaConsumo = financeiroConsumo - radiacao

        tempoPayOff = np.ceil(kitPreco/economiaConsumo) * 30.

        hoje = dt.datetime.today()

        datas = [hoje + dt.timedelta(days=1) for i in range(tempoPayOff)]
        amortizacao = [kitPreco - radiacao for i in range(tempoPayOff)]

        labels = datas
        default = amortizacao
        data = {
            "labels": labels,
            "default": default,

        }
        return Response(data)

def charts(request):

    # nome = request.sessions['name']

    return render(request, 'charts.html', {})
