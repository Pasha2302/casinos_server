from __future__ import annotations

import json

from django.db import transaction
from django.shortcuts import render

from app_casinos.models import (
    GameType, Country, Provider, Game, PaymentMethod, ClassicCurrency, CryptoCurrency, Language, LicensingAuthority,
)


def save_json_data(json_data, path_file):
    with open(path_file, 'w', encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

def download_json_data(path_file) -> list[dict] | dict:
    with open(path_file, encoding="utf-8") as f:
        return json.load(f)


def save_data_to_db(model_class, key_all_data):
    path_file = f"/home/pavelpc/PycharmProjects/Working_Projects/Django_Casinos_Server/{key_all_data}.json"
    data_json = download_json_data(path_file=path_file)
    data_db = model_class.objects.values()
    print(data_db)

    for data_d in data_db:
        for data_j in data_json:
            if data_d['symbol'] == data_j['symbol']:
                try:
                    with transaction.atomic():
                        print(data_j)
                        record = model_class.objects.get(pk=data_d['id'])
                        record.name = data_j['name']
                        record.save()
                        break
                except Exception as err:
                    print(f"Error saving {data_j}: {err}")
                    pass


def index(request):
    save_data_to_db(key_all_data="cryptos1", model_class=CryptoCurrency)
    return render(request, 'app_casinos/base.html', context={"title": "Home"})

