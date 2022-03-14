from django.conf import settings
from django.shortcuts import render
from django.db.models import Max
import requests
import json
from dateutil import parser
from django.urls import reverse
from django.shortcuts import redirect


from .models import CoinMap, QuoteCoin, Status, Coin, FollowCoins

def setup(request):

  if request.user.is_superuser:
    coins = FollowCoins.objects.get(active=True)

    # Create coins
    data_coins = get_coins_info(coins)
    clean_coins_info(data_coins)

    # Map coins with coinmarket cap 
    data_map = get_map_data()
    clean_map_data(data_map)

  return redirect('home')


def get_key():
  """
    Get key to query the api
    returns:
      key
  """
  if settings.PRODUCTION is False:
    key = settings.TEST_KEY
  else:
    key = settings.PROD_KEY
  return key


def get_base_url():
  """
    Get the prefix url to query
    retunrs:
      prefix = Url base to query
  """
  if settings.PRODUCTION is False:
    prefix = 'https://sandbox-api.coinmarketcap.com'
  else:
    prefix = 'https://pro-api.coinmarketcap.com'
  return prefix


def init_session():
  """
    Init a session with the requests library
    Set global headers required by coinmarketcap api

    Returns:
      session = Session instance
  """
  key = get_key()
  headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': key,
    } 

  session = requests.Session()
  session.headers.update(headers)
  return session


def get_data(url, parameters):
  """
    Global get data function
    Query the url with the parameters specified
  """
  session = init_session()
  try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      return data
  except (requests.ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
      print(e)
      return False


def clean_map_data(data):
    inner_info = data['data']

    for row in inner_info:
      row_keys = row.keys()

      if 'first_historical_data' in row_keys:
        first_date = parser.parse(row['first_historical_data'])
      else:
        first_date = None

      if 'last_historical_data' in row_keys:
        last_date = parser.parse(row['last_historical_data'])
      else:
        last_date = None

      if row['platform'] is None:
        platform = ''
      else:
        platform = row['platform']

      if row['rank'] is None:
        rank = 0
      else:
        rank = row['rank']

      print(row['id'])
      print(row['name'])

      coin = Coin.objects.get(external_id = row['id'])

      coin = CoinMap(
        coin = coin,
        extenal_id = row['id'],
        name = row['name'],
        symbol = row['symbol'],
        slug = row['slug'],
        rank = rank,
        is_active = row['is_active'],
        first_historical = first_date,
        last_historical = last_date,
        platform = platform,
        )
      
      coin.save()

    return inner_info


def get_map_data():

  symbol = FollowCoins.objects.get(active=True)

  parameters = {
    'start':'1',
    'limit':'5000',
    'sort': 'cmc_rank',
    'symbol': symbol.coins_string
  }

  url = '/v1/cryptocurrency/map'
  url = get_base_url() + url 
  data = get_data(url, parameters)

  return data


def home(request, currency = 'GTQ'):

  last_update = QuoteCoin.objects.all().aggregate(Max('last_updated_base'))
  quotes = QuoteCoin.objects.filter(
      is_active=1, 
      price__lte=0.50, 
      price__gte=0.0001, 
      currency=currency,
      latest=True
    ).order_by('price')

  context = {
    'quotes': quotes,
    'currency': currency,
    'last_update': last_update['last_updated_base__max']
  }
  return render(request, 'home.html', context=context)


def get_currencys(start = 1, limit = 5000):
  parameters = {
    'start': start,
    'limit': limit
  }

  url = '/v1/fiat/map'
  url = get_base_url() + url
  data = get_data(url, parameters)
  

def get_prices(currency = 'GTQ'):

  coins = CoinMap.get_coins()

  parameters = {
    'id': coins,
    'convert': currency,
  }

  url = '/v2/cryptocurrency/quotes/latest'
  url = get_base_url() + url
  data = get_data(url, parameters)

  return data

  
def clean_prices(data):
  try:
    inner_info = data['data']

    for row in inner_info:
      current_row = inner_info[row]
      current_row_quote = current_row['quote']

      for key in current_row_quote.keys():
        currency = key

      quote = current_row_quote[currency]
      quote_last_update = parser.parse(quote['last_updated'])
      last_update = parser.parse(current_row['last_updated'])

      raw_quotecoin = json.dumps(current_row)
      raw_quote = json.dumps(current_row_quote)

      if current_row['num_market_pairs'] is None:
        num_market_pairs = 0
      else:
        num_market_pairs = current_row['num_market_pairs']

      if current_row['cmc_rank'] is None:
        cmc_rank = 0
      else:
        cmc_rank = current_row['cmc_rank']

      if quote['volume_24h'] is None:
        volume_24h = 0
      else:
        volume_24h = quote['volume_24h']
            
      if quote['volume_change_24h'] is None:
        volume_change_24h = 0
      else:
        volume_change_24h = quote['volume_change_24h']
            
      if quote['percent_change_1h'] is None:
        percent_change_1h = 0
      else:
        percent_change_1h = quote['percent_change_1h']
            
      if quote['percent_change_24h'] is None:
        percent_change_24h = 0
      else:
        percent_change_24h = quote['percent_change_24h']
            
      if quote['percent_change_7d'] is None:
        percent_change_7d = 0
      else:
        percent_change_7d = quote['percent_change_7d']
            
      if quote['percent_change_30d'] is None:
        percent_change_30d = 0
      else:
        percent_change_30d = quote['percent_change_30d']
            
      if quote['percent_change_60d'] is None:
        percent_change_60d = 0
      else:
        percent_change_60d = quote['percent_change_60d']
            
      if quote['percent_change_90d'] is None:
        percent_change_90d = 0
      else:
        percent_change_90d = quote['percent_change_90d']
            
      if quote['market_cap'] is None:
        market_cap = 0
      else:
        market_cap = quote['market_cap']
            
      if quote['market_cap_dominance'] is None:
        market_cap_dominance = 0
      else:
        market_cap_dominance = quote['market_cap_dominance']

      if quote['fully_diluted_market_cap'] is None:
        fully_diluted_market_cap = 0
      else:
        fully_diluted_market_cap = quote['fully_diluted_market_cap']

      coin = Coin.objects.get(external_id = current_row['id'])

      # Only 1 latest per coin
      try:
          old_instance = QuoteCoin.objects.get(coin=coin, latest=True)
          old_instance.latest = False
          old_instance.save()
      except QuoteCoin.DoesNotExist:
          pass

      quote = QuoteCoin (
        coin = coin,
        external_id = current_row['id'],
        name = current_row['name'],
        symbol = current_row['symbol'],
        slug = current_row['slug'],
        num_market_pairs = num_market_pairs,
        is_active = current_row['is_active'],
        cmc_rank = cmc_rank,
        is_fiat = current_row['is_fiat'],
        last_updated_base = last_update,
        raw_quotecoin = raw_quotecoin,
        raw_quote = raw_quote,
        currency = currency,
        price = quote['price'],
        volume_24h = volume_24h,
        volume_change_24h = volume_change_24h,
        percent_change_1h = percent_change_1h,
        percent_change_24h = percent_change_24h,
        percent_change_7d = percent_change_7d,
        percent_change_30d = percent_change_30d,
        percent_change_60d = percent_change_60d,
        percent_change_90d = percent_change_90d,
        market_cap = market_cap,
        market_cap_dominance = market_cap_dominance,
        fully_diluted_market_cap = fully_diluted_market_cap,
        last_updated_quote = quote_last_update,
        latest = True
      )
      quote.save()
    
  except Exception as e:
    print(e)


def get_coins_info(coins):

  parameters = {
    'symbol' : coins,
  }

  url = '/v2/cryptocurrency/info'
  url = get_base_url() + url
  data = get_data(url, parameters)

  return data


def clean_coins_info(data):
  current_row = ''
  
  inner_info = data['data']

  for row in inner_info:
    for coin_x in range(len(inner_info[row])):
      current_row = inner_info[row][coin_x]
      urls = current_row['urls']
      
      if current_row['date_added'] is None:
          date_added = None
      else:
          date_added = parser.parse(current_row['date_added'])

      if current_row['date_launched'] is None:
          date_launched = None
      else:
          date_launched = parser.parse(current_row['date_launched'])
            
      if len(urls['website']) == 0:
          website = '#'
      else:
          website = urls['website'][0]

      if len(urls['technical_doc']) == 0:
          technical_doc = '#'
      else:
          technical_doc = urls['technical_doc'][0]

      if len(urls['twitter']) == 0:
          twitter = '#'
      else:
          twitter = urls['twitter'][0]

      if len(urls['reddit']) == 0:
          reddit = '#'
      else:
          reddit = urls['reddit'][0]

      if len(urls['message_board']) == 0:
          message_board = '#'
      else:
          message_board = urls['message_board'][0]

      if len(urls['announcement']) == 0:
          announcement = '#'
      else:
          announcement = urls['announcement'][0]

      if len(urls['chat']) == 0:
          chat = '#'
      else:
          chat = urls['chat'][0]

      if len(urls['source_code']) == 0:
          source_code = '#'
      else:   
          source_code = urls['source_code'][0]

      coin = Coin(
        external_id = current_row['id'],
        logo = current_row['logo'],
        name = current_row['name'],
        symbol = current_row['symbol'],
        slug = current_row['slug'],
        description = current_row['description'],
        date_added = date_added,
        date_launched = date_launched,
        category = current_row['category'],
        website = website,
        technical_doc = technical_doc,
        twitter = twitter,
        reddit = reddit,
        message_board = message_board,
        announcement = announcement,
        chat = chat,
        source_code = source_code,
      )
      coin.save()
    

def clean_status(data):
  inner_info = data['status']

  timestamp = parser.parse(inner_info['timestamp'])
  error_code = inner_info['error_code']
  error_message = inner_info['error_message']
  elapsed = inner_info['elapsed']
  credit_count = inner_info['credit_count']

  status = Status(
    timestamp = timestamp,
    error_code = error_code,
    error_message = error_message,
    elapsed = elapsed, 
    credit_count = credit_count
  )

  status.save()


def get_error_code(error):

  error = str(error)
  errors = {
    '401': {'code': '1001 [API_KEY_INVALID]', 'message': "This API Key is invalid."},
    '401': {'code': '1002 [API_KEY_MISSING]', 'message': "API key missing."},
    '402': {'code': '1003 [API_KEY_PLAN_REQUIRES_PAYEMENT]', 'message': "Your API Key must be activated. Please go to pro.coinmarketcap.com/account/plan."},
    '402': {'code': '1004 [API_KEY_PLAN_PAYMENT_EXPIRED]', 'message': "Your API Key's subscription plan has expired."},
    '403': {'code': '1005 [API_KEY_REQUIRED]', 'message': "An API Key is required for this call."},
    '403': {'code': '1006 [API_KEY_PLAN_NOT_AUTHORIZED]', 'message': "Your API Key subscription plan doesn't support this endpoint."},
    '403': {'code': '1007 [API_KEY_DISABLED]', 'message': "This API Key has been disabled. Please contact support."},
    '429': {'code': '1008 [API_KEY_PLAN_MINUTE_RATE_LIMIT_REACHED]', 'message': "You've exceeded your API Key's HTTP request rate limit. Rate limits reset every minute."},
    '429': {'code': '1009 [API_KEY_PLAN_DAILY_RATE_LIMIT_REACHED]', 'message': "You've exceeded your API Key's daily rate limit."},
    '429': {'code': '1010 [API_KEY_PLAN_MONTHLY_RATE_LIMIT_REACHED]', 'message': "You've exceeded your API Key's monthly rate limit."},
    '429': {'code': '1011 [IP_RATE_LIMIT_REACHED]', 'message': "You've hit an IP rate limit."},
  }

  if error in errors.keys():
    current_error = errors[error]
    code = current_error['code']
    message = current_error['message']
  else:
    code = 'N/A'
    message = 'N/A'
  
  return {'error': error, 'code': code, 'message': message}


def update_prices():
  currencys = ['USD', 'GTQ']

  for currency in range(len(currencys)):
    current_currency = currencys[currency]
    data = get_prices(current_currency)
    clean_prices(data)
