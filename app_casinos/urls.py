from django.urls import path
from app_casinos.views import (
    views_currency, views_provider, views_country, views_licensing, views_language, views_gameType,
    views_game, views_paymentMethod
)


urlpatterns = [
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


