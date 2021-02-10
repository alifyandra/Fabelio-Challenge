from django.shortcuts import render, redirect
from .models import Product
import difflib

# Create your views here.
def index(request):
    seen = [1]
    products = Product.objects.all()
    last_seen_id = 1
    for p in products:
        if p.id == last_seen_id:
            last_seen = p
            break
    print(products)
    similarity_scores = []
    filtered = [x for x in products if x.id not in seen]
    similar_sorted = sorted(filtered, key=lambda x:
        difflib.SequenceMatcher(None,x.name,last_seen.name).ratio()+
        difflib.SequenceMatcher(None,x.colours,last_seen.colours).ratio()+
        difflib.SequenceMatcher(None,x.material,last_seen.material).ratio(), reverse=True)
    print(similar_sorted)
    response = render(request, 'app/index.html', {'products':similar_sorted,'product':similar_sorted[0]}) 
    return response 