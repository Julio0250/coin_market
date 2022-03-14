from django.db import models
from django.utils.translation import ugettext_lazy as _


class FollowCoins(models.Model):
    coins_string = models.TextField(_("Coins string"))
    active = models.BooleanField(_("Active"), unique=True)
    
    class Meta:
        verbose_name = _("FollowCoins")
        verbose_name_plural = _("FollowCoinss")

    def __str__(self):
        return self.coins_string


class CoinMap(models.Model):
    coin = models.ForeignKey("coins.Coin", on_delete=models.PROTECT)
    extenal_id = models.IntegerField(_("External ID"))
    name = models.CharField(_("Name"), max_length=50)
    symbol = models.CharField(_("Symbol"), max_length=50)
    slug = models.CharField(_("Slug"), max_length=50)
    rank = models.IntegerField(_("Rank"))
    is_active = models.IntegerField(_("Is Active?"))
    first_historical = models.DateTimeField(_("First Historical"), blank=True, null=True)
    last_historical = models.DateTimeField(_("Last Historical"), blank=True, null=True)
    platform = models.TextField(_("Platform"))

    class Meta:
        verbose_name = _("CoinMap")
        verbose_name_plural = _("CoinMaps")

    def get_coins():
        coins_map = CoinMap.objects.all()
        coins = ''

        for map in coins_map:
            coins = coins + str(map.extenal_id) + ','

        coins = coins[:-1]
        
        return coins



class Currency(models.Model):
    external_id = models.IntegerField(_("External ID"))
    name = models.CharField(_("Name"), max_length=50)
    sign = models.CharField(_("Sign"), max_length=50)
    symbol = models.CharField(_("Symbol"), max_length=50)
    
    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencys")


class QuoteCoin(models.Model):
    coin = models.ForeignKey("coins.Coin", on_delete=models.PROTECT)
    external_id = models.IntegerField(_("External ID"))
    name = models.CharField(_("Name"), max_length=50)
    symbol = models.CharField(_("Symbol"), max_length=50)
    slug = models.CharField(_("Slug"), max_length=50)
    num_market_pairs = models.DecimalField(_("Num Market Pairs"), max_digits=35, decimal_places=12)
    is_active = models.IntegerField(_("Is Active?"))
    cmc_rank = models.IntegerField(_("Rank"))
    is_fiat = models.IntegerField(_("Is FIAT?"))
    last_updated_base = models.DateTimeField(_("Last Updated"), blank=True, null=True)
    raw_quotecoin = models.TextField()
    raw_quote = models.TextField()
    currency = models.CharField(_("Currency"), max_length=50)
    price = models.DecimalField(max_digits=35, decimal_places=12)
    volume_24h = models.DecimalField(max_digits=35, decimal_places=12)
    volume_change_24h = models.DecimalField(max_digits=35, decimal_places=12)
    percent_change_1h = models.DecimalField(max_digits=35, decimal_places=12)
    percent_change_24h = models.DecimalField(max_digits=35, decimal_places=12)
    percent_change_7d = models.DecimalField(max_digits=35, decimal_places=12)
    percent_change_30d = models.DecimalField(max_digits=35, decimal_places=12)
    percent_change_60d = models.DecimalField(max_digits=35, decimal_places=12)
    percent_change_90d = models.DecimalField(max_digits=35, decimal_places=12)
    market_cap = models.DecimalField(max_digits=35, decimal_places=12)
    market_cap_dominance = models.DecimalField(max_digits=35, decimal_places=12)
    fully_diluted_market_cap = models.DecimalField(max_digits=35, decimal_places=12)
    last_updated_quote = models.DateTimeField()
    latest = models.BooleanField(_("Latest"))
    
    class Meta:
        verbose_name = _("QuoteCoin")
        verbose_name_plural = _("QuoteCoins")


class Coin(models.Model):
    external_id = models.IntegerField(_("External ID"))
    logo = models.CharField(_("Logo"), max_length=400)
    name = models.CharField(_("Name"), max_length=100)
    symbol = models.CharField(_("Symbol"), max_length=50)
    slug = models.CharField(_("Slug"), max_length=50)
    description = models.TextField(_("Description"), max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(_("Date Added"), blank=True, null=True)
    date_launched = models.DateTimeField(_("Date Launched"), blank=True, null=True)
    category = models.CharField(_("Category"), max_length=50)
    website = models.CharField(_("Logo"), max_length=400)
    technical_doc = models.CharField(_("Technical Doc"), max_length=400)
    twitter = models.CharField(_("Twitter"), max_length=400)
    reddit = models.CharField(_("Reddit"), max_length=400)
    message_board = models.CharField(_("Message Board"), max_length=400)
    announcement = models.CharField(_("Announcement"), max_length=400)
    chat = models.CharField(_("Chat"), max_length=400)
    source_code =  models.CharField(_("Source Code"), max_length=400)
    
    class Meta:
        verbose_name = _("Coin")
        verbose_name_plural = _("Coins")

class Status(models.Model):
    timestamp = models.DateTimeField(_("Timestamp"))
    error_code = models.CharField(_("Error Code"), max_length=50)
    error_message = models.CharField(_("Error Message"), max_length=500)
    elapsed = models.DecimalField(_("Elapsed"), max_digits=10, decimal_places=2)
    credit_count = models.IntegerField(_("Credit Count"))

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Status")

