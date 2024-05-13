from django.urls import path
from app_casinos.views import (
    views_currency, views_provider, views_country, views_licensing, views_language, views_gameType,
    views_game, views_paymentMethod, views_test, views_auto_fill_bonus
)


urlpatterns = [
    path('get_data/', views_test.get_data, name='get_data'),

    # path('currency_data-classic/', views_currency.CurrencyDataAPIView.as_view(), name='currency-data'),
    path('currency-classic/', views_currency.CurrencyListCreateAPIView.as_view(), name='currency-list-create'),
    path('delete_all_data-currency/', views_currency.DeleteAllDataCurrencyAPIView.as_view(), name='delete_all_data'),

    path('currency-crypto/', views_currency.CryptoCurrencyListCreateAPIView.as_view(),
         name='crypto-currency-list-create'),

    # ================================================================================================================ #
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


    path('game/', views_game.GameListCreateAPIView.as_view(), name='game-list-create'),
    path('game-filter/', views_game.GameFilterAPIView.as_view(), name='game-filter'),

    path(
        'data-autofill-bonus/create/',
        views_auto_fill_bonus.DataAutoFillBonusViewSet.as_view({'post': 'create'}),
        name='data-autofill-bonus-create'
    ),
    path(
        'data-autofill-bonus/<str:pk>/',
        views_auto_fill_bonus.DataAutoFillBonusViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
        name='data-autofill-bonus'
    ),

    path('paymentmethod/', views_paymentMethod.PaymentMethodListCreateAPIView.as_view(),
             name='paymentmethod-list-create'),
]
