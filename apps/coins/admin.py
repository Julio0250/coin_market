from django.contrib import admin
from .models import FollowCoins, Coin, CoinMap, QuoteCoin

# Register your models here.
admin.site.register(FollowCoins)
admin.site.register(Coin)
admin.site.register(CoinMap)
admin.site.register(QuoteCoin)