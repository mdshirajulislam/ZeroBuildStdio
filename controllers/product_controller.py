from utils.response_util import send_json_response, parse_request_body
from firebase_config import db, mock_db
import uuid

def create_product(handler):
    body = parse_request_body(handler)
    shop_id = body.get("shop_id")
    name = body.get("name")
    price = body.get("price")
    old_price = body.get("old_price", None)
    image_url = body.get("image_url", "https://images.unsplash.com/photo-1556821840-3a63f95609a7?q=80&w=600&auto=format&fit=crop")
    badge = body.get("badge", "")
    brand = body.get("brand", "")
    category = body.get("category", "")
    
    if not shop_id or not name or price is None:
        send_json_response(handler, 400, {"error": "shop_id, name, and price required"})
        return
        
    product_id = str(uuid.uuid4())
    product_data = {
        "id": product_id,
        "shop_id": shop_id,
        "name": name,
        "price": price,
        "old_price": old_price,
        "image_url": image_url,
        "badge": badge,
        "brand": brand,
        "category": category
    }
    
    if db:
        try:
            db.collection("products").document(product_id).set(product_data)
            send_json_response(handler, 201, {"message": "Product added", "product": product_data})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        mock_db["products"].append(product_data)
        send_json_response(handler, 201, {"message": "Mock Product added", "product": product_data})

def get_products(handler):
    if db:
        try:
            products_ref = db.collection("products")
            docs = products_ref.stream()
            products = [doc.to_dict() for doc in docs]
            send_json_response(handler, 200, {"products": products})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        send_json_response(handler, 200, {"products": mock_db["products"]})

def get_products_for_shop(shop_id):
    if db:
        products_ref = db.collection("products")
        query = products_ref.where("shop_id", "==", shop_id)
        docs = query.stream()
        return [doc.to_dict() for doc in docs]
    else:
        return [p for p in mock_db["products"] if p["shop_id"] == shop_id]

def add_demo_products(shop_id):
    demos = [
        {
            "id": str(uuid.uuid4()), "shop_id": shop_id, "name": "Earth Element - Graphic Tee", "price": 380.00, "old_price": 450.00,
            "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=600&auto=format&fit=crop", "badge": "stolen"
        },
        {
            "id": str(uuid.uuid4()), "shop_id": shop_id, "name": "SPIDERMAN - Superhero Tshirt", "price": 380.00, "old_price": 450.00,
            "image_url": "https://images.unsplash.com/photo-1562157873-818bc0726f68?q=80&w=600&auto=format&fit=crop", "badge": "stolen"
        },
        {
            "id": str(uuid.uuid4()), "shop_id": shop_id, "name": "Naruto- Anime Tshirt", "price": 380.00, "old_price": 450.00,
            "image_url": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?q=80&w=600&auto=format&fit=crop", "badge": "stolen"
        },
        {
            "id": str(uuid.uuid4()), "shop_id": shop_id, "name": "BANGLADESH Printed TSHIRT", "price": 380.00, "old_price": 450.00,
            "image_url": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?q=80&w=600&auto=format&fit=crop", "badge": "stolen"
        }
    ]
    if db:
        for p in demos:
            db.collection("products").document(p["id"]).set(p)
    else:
        mock_db["products"].extend(demos)

def update_product(handler, product_id):
    body = parse_request_body(handler)
    if db:
        try:
            doc_ref = db.collection("products").document(product_id)
            if not doc_ref.get().exists:
                send_json_response(handler, 404, {"error": "Product not found"})
                return
            doc_ref.update(body)
            send_json_response(handler, 200, {"message": "Product updated"})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        for p in mock_db["products"]:
            if p["id"] == product_id:
                p.update(body)
                send_json_response(handler, 200, {"message": "Product updated"})
                return
        send_json_response(handler, 404, {"error": "Product not found"})

def delete_product(handler, product_id):
    if db:
        try:
            db.collection("products").document(product_id).delete()
            send_json_response(handler, 200, {"message": "Product deleted"})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        mock_db["products"] = [p for p in mock_db["products"] if p["id"] != product_id]
        send_json_response(handler, 200, {"message": "Product deleted"})
