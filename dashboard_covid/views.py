from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


# Create your views here.

def dashboard(request):
    """Funzione che prende i dati e manda al template della dashboard"""
    df = pd.read_json('https://query.data.world/s/lbd7qh3tc3eou7oxvwywpi27znqpns')
    df_province = pd.read_json('https://query.data.world/s/rcatyiw4uwlpm545mrwwf7oaudyeys')
    df_province = df_province[df_province['denominazione_regione'] =='Sardegna']
    df_ss = df_province.loc[df_province['sigla_provincia'] == "SS"]
    df_ca = df_province.loc[df_province['sigla_provincia'] == "CA"]
    df_or = df_province.loc[df_province['sigla_provincia'] == "OR"]
    df_su = df_province.loc[df_province['sigla_provincia'] == "SU"]
    df_nu = df_province.loc[df_province['sigla_provincia'] == "NU"]
    df_ss.index = df_ss['data']
    df_ss.drop(['data'], axis=1, inplace=True)
    df_ca.index = df_ca['data']
    df_ca.drop(['data'], axis=1, inplace=True)
    df_or.index = df_or['data']
    df_or.drop(['data'], axis=1, inplace=True)
    df_su.index = df_su['data']
    df_su.drop(['data'], axis=1, inplace=True)
    df_nu.index = df_nu['data']
    df_nu.drop(['data'], axis=1, inplace=True)
    df_ca = df_ca.pivot(columns='sigla_provincia', values='totale_casi')
    df_ss = df_ss.pivot(columns='sigla_provincia', values='totale_casi')
    df_nu = df_nu.pivot(columns='sigla_provincia', values='totale_casi')
    df_or = df_or.pivot(columns='sigla_provincia', values='totale_casi')
    df_su = df_su.pivot(columns='sigla_provincia', values='totale_casi')
    df_province = pd.concat([df_ca, df_ss, df_nu, df_or, df_su], axis=1).reindex(df_ca.index)

    context={
        'data':list(df['data'].values),
        'stato':list(df['stato'].values),
        'ricoverati_con_sintomi':list(df['ricoverati_con_sintomi'].values),
        'terapia_intensiva':list(df['terapia_intensiva'].values),
        'totale_ospedalizzati':list(df['totale_ospedalizzati'].values),
        'isolamento_domiciliare':list(df['isolamento_domiciliare'].values),
        'totale_positivi':list(df['totale_positivi'].values),
        'variazione_totale_positivi':list(df['variazione_totale_positivi'].values),
        'nuovi_positivi':list(df['nuovi_positivi'].values),
        'dimessi_guariti':list(df['dimessi_guariti'].values),
        'deceduti':list(df['deceduti'].values),
        'casi_da_sospetto_diagnostico':list(df['casi_da_sospetto_diagnostico'].values),
        'casi_da_screening':list(df['casi_da_screening'].values),
        'totale_casi':list(df['totale_casi'].values),
        'tamponi':list(df['tamponi'].values),
        'casi_testati':list(df['casi_testati'].values),
        'note':list(df['note'].values),
        'ingressi_terapia_intensiva':list(df['ingressi_terapia_intensiva'].values),
        'note_test':list(df['note_test'].values),
        'note_casi':list(df['note_casi'].values),
        'Casi_Cagliari': list(df_province['CA'].values),
        'Casi_Sassari': list(df_province['SS'].values),
        'Casi_Nuoro': list(df_province['NU'].values),
        'Casi_Oristano': list(df_province['OR'].values),
        'Casi_Sud_Sardegna': list(df_province['SU'].values),
        'data_provincie': list(df_province.index.values)
    }

    return render(request,'dashboard_covid/dashboard.html',context=context)