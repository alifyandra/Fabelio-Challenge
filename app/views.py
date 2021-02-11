from django.shortcuts import render, redirect
from .models import *
import difflib

# Create your views here.
def index(request):
    try:
        customer = request.user.customer
    except:
        try:
            device = request.COOKIES['device']
        except:
            # First time opening page forces a reload to create a cookie from the script in base.html
            return render(request, 'app/index.html', {'products':[],'product':[]})
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    
    # List of seen product id's
    seen = customer.seen
    last_seen_id = seen[-1] if seen else 1

    products = Product.objects.all().order_by('id')
    filtered = [x for x in products if x.id not in seen]

    # Set last seen variable to hold the last seen product object
    for p in products:
        if p.id == last_seen_id:
            last_seen = p
            break
    
    # Similarity sort algorithm
    similar_sorted = sorted(filtered, key=lambda x:
        difflib.SequenceMatcher(None,x.name,last_seen.name).ratio()+
        difflib.SequenceMatcher(None,x.colours,last_seen.colours).ratio()+
        difflib.SequenceMatcher(None,x.material,last_seen.material).ratio(), reverse=True)
    
    # Add newly seen product id if not final object to be seen
    if len(filtered) > 1:
        customer.seen.append(similar_sorted[0].id)
    else:
        customer.seen = []
    customer.save()

    return render(request, 'app/index.html', {'products':similar_sorted[1:],'product':similar_sorted[0], "last_product":last_seen, 'first_product':True if len(seen) == 1 else False})  