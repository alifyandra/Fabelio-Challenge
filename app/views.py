from django.shortcuts import render, redirect
from .models import *
import difflib

# Create your views here.
def index(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    
    seen = customer.seen
    products = Product.objects.all()
    filtered = [x for x in products if x.id not in seen]
    last_seen_id = seen[-1] if seen else 1

    for p in products:
        if p.id == last_seen_id:
            last_seen = p
            break

    similarity_scores = []
    similar_sorted = sorted(filtered, key=lambda x:
        difflib.SequenceMatcher(None,x.name,last_seen.name).ratio()+
        difflib.SequenceMatcher(None,x.colours,last_seen.colours).ratio()+
        difflib.SequenceMatcher(None,x.material,last_seen.material).ratio(), reverse=True)
    
    if len(filtered) > 1:
        customer.seen.append(similar_sorted[0].id)
    else:
        customer.seen = []
    customer.save()

    return render(request, 'app/index.html', {'products':similar_sorted,'product':similar_sorted[0]})  