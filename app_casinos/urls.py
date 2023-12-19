from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name="index"),

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

]


# Добавление URL-паттернов для обслуживания статических файлов в отладочном режиме
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)