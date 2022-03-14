# Generated by Django 3.2 on 2022-03-13 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(verbose_name='External ID')),
                ('logo', models.CharField(max_length=400, verbose_name='Logo')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('symbol', models.CharField(max_length=50, verbose_name='Symbol')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('date_added', models.DateTimeField(blank=True, null=True, verbose_name='Date Added')),
                ('date_launched', models.DateTimeField(blank=True, null=True, verbose_name='Date Launched')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('website', models.CharField(max_length=400, verbose_name='Logo')),
                ('technical_doc', models.CharField(max_length=400, verbose_name='Logo')),
                ('twitter', models.CharField(max_length=400, verbose_name='Logo')),
                ('reddit', models.CharField(max_length=400, verbose_name='Logo')),
                ('message_board', models.CharField(max_length=400, verbose_name='Logo')),
                ('announcement', models.CharField(max_length=400, verbose_name='Logo')),
                ('chat', models.CharField(max_length=400, verbose_name='Logo')),
                ('source_code', models.CharField(max_length=400, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Coin',
                'verbose_name_plural': 'Coins',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(verbose_name='External ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('sign', models.CharField(max_length=50, verbose_name='Sign')),
                ('symbol', models.CharField(max_length=50, verbose_name='Symbol')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencys',
            },
        ),
        migrations.CreateModel(
            name='FollowCoins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins_string', models.CharField(max_length=500, verbose_name='Coins string')),
                ('active', models.BooleanField(unique=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'FollowCoins',
                'verbose_name_plural': 'FollowCoinss',
            },
        ),
        migrations.CreateModel(
            name='QuoteCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(verbose_name='External ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('symbol', models.CharField(max_length=50, verbose_name='Symbol')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('num_market_pairs', models.DecimalField(decimal_places=12, max_digits=35, verbose_name='Num Market Pairs')),
                ('is_active', models.IntegerField(verbose_name='Is Active?')),
                ('cmc_rank', models.IntegerField(verbose_name='Rank')),
                ('is_fiat', models.IntegerField(verbose_name='Is FIAT?')),
                ('last_updated_base', models.DateTimeField(blank=True, null=True, verbose_name='Last Updated')),
                ('raw_quotecoin', models.TextField()),
                ('raw_quote', models.TextField()),
                ('currency', models.CharField(max_length=50, verbose_name='Currency')),
                ('price', models.DecimalField(decimal_places=12, max_digits=35)),
                ('volume_24h', models.DecimalField(decimal_places=12, max_digits=35)),
                ('volume_change_24h', models.DecimalField(decimal_places=12, max_digits=35)),
                ('percent_change_1h', models.DecimalField(decimal_places=12, max_digits=35)),
                ('percent_change_24h', models.DecimalField(decimal_places=12, max_digits=35)),
                ('percent_change_7d', models.DecimalField(decimal_places=12, max_digits=35)),
                ('percent_change_30d', models.DecimalField(decimal_places=12, max_digits=35)),
                ('percent_change_60d', models.DecimalField(decimal_places=12, max_digits=35)),
                ('percent_change_90d', models.DecimalField(decimal_places=12, max_digits=35)),
                ('market_cap', models.DecimalField(decimal_places=12, max_digits=35)),
                ('market_cap_dominance', models.DecimalField(decimal_places=12, max_digits=35)),
                ('fully_diluted_market_cap', models.DecimalField(decimal_places=12, max_digits=35)),
                ('last_updated_quote', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'QuoteCoin',
                'verbose_name_plural': 'QuoteCoins',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp')),
                ('error_code', models.CharField(max_length=50, verbose_name='Error Code')),
                ('error_message', models.CharField(max_length=500, verbose_name='Error Message')),
                ('elapsed', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Elapsed')),
                ('credit_count', models.IntegerField(verbose_name='Credit Count')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='CoinMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extenal_id', models.IntegerField(verbose_name='External ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('symbol', models.CharField(max_length=50, verbose_name='Symbol')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('is_active', models.IntegerField(verbose_name='Is Active?')),
                ('first_historical', models.DateTimeField(blank=True, null=True, verbose_name='First Historical')),
                ('last_historical', models.DateTimeField(blank=True, null=True, verbose_name='Last Historical')),
                ('platform', models.TextField(verbose_name='Platform')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coins.coin')),
            ],
            options={
                'verbose_name': 'CoinMap',
                'verbose_name_plural': 'CoinMaps',
            },
        ),
    ]