import requests
from django.shortcuts import render
from django.conf import settings

def home(request):
    try:
        # Fetch stores from the Brighton API
        response = requests.get(settings.BRIGHTON_FEED_URL)
        response.raise_for_status()
        stores = response.json()
        
        # Create store list for template
        store_list = [
            {
                'id': store_data['storeId'],
                'name': store_data['name'],
                'name2': store_data['name2'],
                'image': store_data['mainImageUrl'],
                'viewstore_url': store_data['viewstoreUrl'],
                'address1': store_data['address1'],
                'city': store_data['city'],
                'state': store_data['state'],
            }
            for store_id, store_data in stores.items()
        ]
        
        return render(request, 'store/home.html', {
            'stores': store_list
        })
        
    except requests.RequestException as e:
        print(f"Error fetching store data: {str(e)}")
        return render(request, 'store/home.html', {
            'error': f"Error fetching store data: {str(e)}"
        })