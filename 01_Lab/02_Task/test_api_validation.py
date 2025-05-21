import requests
import pytest

# API endpoint
API_URL = "https://fakestoreapi.com/products"

def test_server_response():
    """Test if the server responds with status code 200"""
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_product_attributes():
    """Test if all products have valid attributes"""
    response = requests.get(API_URL)
    products = response.json()
    
    defective_products = []
    
    for product in products:
        defects = []
        
        # Check if title is empty
        if not product.get('title'):
            defects.append("Empty title")
            
        # Check if price is negative
        if product.get('price', 0) < 0:
            defects.append("Negative price")
            
        # Check if rating.rate exceeds 5
        rating = product.get('rating', {})
        if rating.get('rate', 0) > 5:
            defects.append("Rating rate exceeds 5")
            
        if defects:
            defective_products.append({
                'id': product.get('id'),
                'title': product.get('title'),
                'defects': defects
            })
    
    # Print defective products if any found
    if defective_products:
        print("\nDefective Products Found:")
        for product in defective_products:
            print(f"Product ID: {product['id']}")
            print(f"Title: {product['title']}")
            print(f"Defects: {', '.join(product['defects'])}")
            print("-" * 50)
    
    # Assert that no defective products were found
    assert len(defective_products) == 0, f"Found {len(defective_products)} products with defects" 