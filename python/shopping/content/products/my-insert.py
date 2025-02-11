from __future__ import print_function
import sys
import json

# The common module provides setup functionality used by the samples,
# such as authentication and unique id generation.
from shopping.content import common
from shopping.content.products.tools.db_calls import get_womenclothes
from shopping.content.products.tools import analyze_variants

# Define the UINT32 max value
UINT32_MAX = 4294967295

# function to be called
func_call = get_womenclothes()
# list to add
products = []

googleProductCategory = 'Clothing & Accessories > Clothing'  # product category

# Start of code to create product batch entry
for product in func_call:
    # Analyze the variants once
    variants = analyze_variants(product['variants'])[0]
    
    for color, sizes in variants.items():
        # Generate a valid UINT32 batch_id
        batch_id = int(common.get_unique_id()) % (UINT32_MAX + 1)  # Ensure within UINT32 range
        offer_id = 'item#{}'.format(common.get_unique_id())  # Use .format for clarity
        
        # Add the product entry
        products.append({
            "batchId": batch_id,  # Make sure this is a numeric ID (UINT32)
            "merchantId": 5540377362,  # merchant ID
            "method": "insert",
            "product": {  # Use "product" as a string key
                "offerId": offer_id,
                "title": product['title'],
                "description": product['description'],
                "link": f"https://www.liziestyle.com/product_detail/{product['_id']}",
                "imageLink": product['images'][0],
                "contentLanguage": 'it',
                "targetCountry": 'IT',
                "channel": 'online',
                "availability": 'in stock',
                "color": color,
                "condition": 'new',
                "googleProductCategory": googleProductCategory,
                "price": {
                    "value": product['price'],
                    "currency": 'EUR'
                },
                "sizes": sizes,
                "shipping": [{
                    "country": 'IT',  # Corrected the shipping country to IT
                    'service': 'Standard shipping',
                    'price': {
                        'value': '5',
                        'currency': 'EUR'
                    }
                }],
                "shippingWeight": {
                    'value': product['weight'],
                    'unit': 'grams'
                }
            }
        })
        
# print(products)

def main(argv):
    # Authenticate and construct service.
    service, config, _ = common.init(argv, __doc__)
    merchant_id = config['merchantId']
    batch = {
        "entries": products
    }

    request = service.products().custombatch(body=batch)
    result = request.execute()

    if result['kind'] == 'content#productsCustomBatchResponse':
        entries = result['entries']
        for entry in entries:
            product = entry.get('product')
            errors = entry.get('errors')
            if product:
                print(f'Product "{product["id"]}" with offerId "{product["offerId"]}" was created.')
            elif errors:
                print(f'Errors for batch entry {entry["batchId"]}:')
                print(json.dumps(errors, sort_keys=True, indent=2, separators=(',', ': ')))
    else:
        print(f'There was an error. Response: {result}')
    
    # FOR TEST PURPOSES
    # print(result.get('entries')) 

if __name__ == '__main__':
    main(sys.argv)






# run command below to activate code and insert in google shopping
# python -m shopping.content.products.my-insert
