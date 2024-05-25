from django.urls import path
from app_casinos.views import (
    views_game, views_test, views_auto_fill_bonus, views_casino
)
from app_casinos.views.views_start_parser import ParserView

urlpatterns = [
    path('get_data/', views_test.get_data, name='get_data'),

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

    path('casino-pars/', views_casino.CasinoFilteredListAPIView.as_view(), name='casino-pars'),
    path(
        'casino-update/<slug:slug>/', views_casino.CasinoRetrieveUpdateAPIView.as_view(),
        name='casino-update-fields'
    ),
    path('add-data-casino/', views_casino.AddDataCasinoAPIView.as_view()),

    path('get-token2302/', views_casino.CSRFTokenAPIView.as_view()),

    path('start-parser/', ParserView.as_view(), name='parser_view'),
]
