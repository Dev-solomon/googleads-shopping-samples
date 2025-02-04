from pymongo import DESCENDING
from shopping.content.products.tools.product_model import Product



# func to get women clothes from database
def get_womenclothes():
    try:
        
        # Fetch products from the collection based on query and pagination
        products_list = list(Product.collection.find({"category": "womens"}).sort("createdAt", DESCENDING))
        
       
        
        return products_list

    except Exception as e:
        return print({"message": str(e)})

# func to get men clothes
def get_menclothes():
    try:
        
        # Fetch products from the collection based on query and pagination
        products_list = list(Product.collection.find({"category": "mens"}).sort("createdAt", DESCENDING))
        
       
        
        return products_list

    except Exception as e:
        return print({"message": str(e)})
    
# func to get shoes from database
def get_shoes():
    try:
        
        # Fetch products from the collection based on query and pagination
        products_list = list(Product.collection.find({"category": "shoes"}).sort("createdAt", DESCENDING))
        
       
        
        return products_list

    except Exception as e:
        return print({"message": str(e)})
    
# func to get accessories from database
def get_jewelries():
    try:
        
        # Fetch products from the collection based on query and pagination
        products_list = list(Product.collection.find({"category": "accessories"}).sort("createdAt", DESCENDING))
        
       
        
        return products_list

    except Exception as e:
        return print({"message": str(e)})
    
    
# func to get household products
def get_household():
    try:
        
        # Fetch products from the collection based on query and pagination
        products_list = list(Product.collection.find({"category": "household"}).sort("createdAt", DESCENDING))
        
       
        
        return products_list

    except Exception as e:
        return print({"message": str(e)})
    
  
#   func to get beauty products from database  
def get_beauty():
    try:
        
        # Fetch products from the collection based on query and pagination
        products_list = list(Product.collection.find({"category": "beauty"}).sort("createdAt", DESCENDING))
        
       
        
        return products_list

    except Exception as e:
        return print({"message": str(e)})