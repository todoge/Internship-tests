from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from result.models import Result
from result.form import RawGuessForm
import requests
from django.utils import timezone

# Create your views here.
def homepage_view(request, *args, **kwargs):
    message = ""
    guess_price = 0
    actual_price = 0
    is_valid = False
    results = []

    if request.user.is_authenticated:
        results = Result._meta.model.objects.filter(author=request.user).order_by('-created_at')

    if request.method == "POST":
        form = RawGuessForm(request.POST)
        if form.is_valid():
            data = request.POST
            coin_id = get_id(data["coin"])
            guess_price = data["guess_price"]
            url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + coin_id + '&vs_currencies=usd'
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    is_valid = True
                    actual_price = response.json()[coin_id]["usd"]
                    if request.user.is_authenticated:
                        now = timezone.now()
                        result = Result.objects.create_result(coin=coin_id, guess_price=guess_price, actual_price=actual_price, author=request.user, created_at=now)
                        results = Result._meta.model.objects.filter(author=request.user).order_by('-created_at')
                        Result.save(result)
                except:
                    is_valid = False
                    message = "Not a valid coin!"
            else:
                is_valid = False
                message = "API error! Please try again later."
        else:
            is_valid = False
            message = "Please enter a valid coin and price"

    page = request.GET.get('page', 1)
    paginator = Paginator(results, 5)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
        
    context = {
        'history' : results,
        'guess_result' : {
            'is_valid' : is_valid,
            "guess_price" : float(guess_price),
            "actual_price" : float(actual_price),
            "message" : message
        }
    }

    return render(request, "homepage.html", context)

def get_id(coin_name):
    coin = coin_name.strip().lower()
    return coin.replace(" ", "-")
    

# def convert_to_localtime(utctime):
#     fmt = '%d/%m/%Y %H:%M'
#     ltz = tzlocal.get_localzone()
#     localtz = utc.replace(tzinfo=pytz.utc).astimezone(ltz)
#     return localtz.strftime(fmt)