import requests

endPoint = 'https://automationexercise.com'
list_product = []


def test_verify_endPoint():
    response = requests.get(endPoint)
    assert response.status_code == 200

def test_get_all_product_list():
    product_response = requests.get(endPoint + "/api/productsList")
    assert product_response.status_code == 200
    products = product_response.json()
    print(products)
    list_product.append(products)

def test_post_to_all_product_list():
    product_response = requests.post(endPoint + "/api/productsList")
    assert product_response.status_code == 200
    message = product_response.text
    assert message == '{"responseCode": 405, "message": "This request method is not supported."}'
    print(message)
