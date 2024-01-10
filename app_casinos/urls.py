from django.urls import path
from app_casinos.views import (
     # REVIEW: мешаешь snake_case и camelCase в views_gameType и views_paymentMethod
    views_currency, views_provider, views_country, views_licensing, views_language, views_gameType,
    views_game, views_paymentMethod
)

# REVIEW: принцип должен быть такой, что мы идём от общего к частному. Но располагаем первичную информацию в начале
# Например, в первую очередь нам важно, что разговор идёт о валюте: currency/
# Дальше можно уточнить, что речь о крипте: currency/crypto/
# Можно уточнить, что нас интересует что-то ещё более специфичное: currency/crypto/btc/
# Хотя тут мы можем уменьшить глубину: currency/btc/

# Дальше нужно определиться, что именно мы делаем. Самый лучший вариант — HTTP-методы:
# GET (получение), POST (создание), PUT (Обновление), PATCH (частичное обновление), DELETE (удаление)
# Если просто метода не хвататет, можно выделить путь: currency/delete-all (можно комбинироваться с методом DELETE)

# Также я бы рассмотрел вариант указать корень во множественном числе: currencies. Так будет правильно,
# хотя длиннее и сложнее писать


urlpatterns = [
    # path('currency_data-classic/', views_currency.CurrencyDataAPIView.as_view(), name='currency-data'),
    path('currency-classic/', views_currency.CurrencyListCreateAPIView.as_view(), name='currency-list-create'),
    # REVIEW: тут и _ и -
    path('delete_all_data-currency/', views_currency.DeleteAllDataCurrencyAPIView.as_view(), name='delete_all_data'),

    path('currency-crypto/', views_currency.CryptoCurrencyListCreateAPIView.as_view(),
         name='crypto-currency-list-create'),

     # REVIEW: почему не currency/crypto/ и currency/classic/ или currency/fiat/?

    # ================================================================================================================ #
    # REVIEW: Если по запросу мы получаем список, то странно, что в URL название сущности в ед. ч.
    # Должно быть providers/. Если мы потом хотим получить конкретного провайдера, то уже providers/:id/
    path('provider/', views_provider.ProviderListCreateAPIView.as_view(),
         name='provider-list-create'),

    path('country/', views_country.CountryListCreateAPIView.as_view(),
         name='country-list-create'),

    path('licensing/', views_licensing.LicensingAuthorityListCreateAPIView.as_view(),
             name='licensing-list-create'),

    path('language/', views_language.LanguageListCreateAPIView.as_view(),
             name='language-list-create'),

    path('gametype/', views_gameType.GameTypeListCreateAPIView.as_view(),
             name='gametype-list-create'),

    path('game/', views_game.GameListCreateAPIView.as_view(),
             name='game-list-create'),

    path('paymentmethod/', views_paymentMethod.PaymentMethodListCreateAPIView.as_view(),
             name='paymentmethod-list-create'),
]



# urlpatterns = [
#     path('', views.index, name="index"),

    # path('api/v1/add-get-games', views.GamesListCreateView.as_view()),
    # path('api/v1/update-games/<int:pk>', views.GamesAPIUpdate.as_view()),
    # path('api/v1/add-provider-to-games/<int:pk>', views.AddProviderToGameView.as_view()),
    #
    #
    # path('api/v1/add-get-provider', views.ProviderListCreateView.as_view()),
    # path('api/v1/add-get-vendor', views.VendorListCreateView.as_view()),
    # path('api/v1/add-get-category-games', views.CategoryGamesListCreateView.as_view()),
    #
    # path('api/v1/add-get-bonuses', views.BonusesListCreateView.as_view()),
    # path('api/v1/add-get-general-tc', views.GeneralTCListCreateView.as_view()),
    # path('api/v1/add-get-bonus-tc', views.BonusTCListCreateView.as_view()),
    #
    #
    # path('api/v1/get-casino/<int:pk>', views.CasinoAPIView.as_view()),
    # path('api/v1/update-casino/<int:pk>', views.CasinoAPIUpdate.as_view()),
    #
    #
    # path("show/game/<int:pk>", views.show_game, name="show_game"),
    #
    # path("show/bonus-html/<int:pk>", views.show_bonus_html_field, name="show_bonus_html_field"),
    # path("show/bonus-tc-html/<int:pk>", views.show_bonus_tc_html_field, name="show_bonus_tc_html_field"),
    # path("show/general-tc-html/<int:pk>", views.show_general_tc_html_field, name="show_general_tc_html_field"),

    # path('api/v1/get-add-slots', views.SlotsAPIGetPost.as_view()),

    # path('api/v1/update-slots/<int:pk>', views.SlotsAPIUpdate.as_view()),
    #
    # path('api/v1/retrieve-update-destroy-slots/<int:pk>', views.SlotsAPIDetailView.as_view()),

# ]


