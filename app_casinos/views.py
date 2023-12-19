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
    data_json = download_json_data(path_file=path_file)['crypto_codes']

    for data in data_json:
        try:
            with transaction.atomic():
                print(data)
                # new_obj = model_class(name=data)
                new_obj = model_class(symbol=data)
                # Сохранение объекта в базе данных
                new_obj.save()
        except Exception as err:
            print(f"Error saving {data}: {err}")
            pass


def index(request):
    save_data_to_db(key_all_data="crypto_codes", model_class=CryptoCurrency)
    return render(request, 'app_casinos/base.html', context={"title": "Home"})

