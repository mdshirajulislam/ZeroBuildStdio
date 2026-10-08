from utils.response_util import send_json_response, parse_request_body
from firebase_config import db, mock_db
import uuid
from controllers.product_controller import add_demo_products

def create_shop(handler):
    body = parse_request_body(handler)
    shop_name = body.get("name")
    owner_email = body.get("email")
    subdomain = body.get("subdomain")
    theme = body.get("theme", "stolen")
    
    if not shop_name or not owner_email or not subdomain:
        send_json_response(handler, 400, {"error": "Shop name, email, and subdomain are required"})
        return
        
    shop_id = str(uuid.uuid4())
    shop_data = {
        "id": shop_id,
        "name": shop_name,
        "email": owner_email,
        "subdomain": subdomain,
        "theme": theme,
        "status": "active",
        "settings": {
            "hero_title": f"Welcome to {shop_name}",
            "hero_subtitle": "The best place to buy amazing products.",
            "primary_color": "#ffe000",
            "banner_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1200&auto=format&fit=crop",
            "categories": [
                {"name": "Polo Tshirt", "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=200&auto=format&fit=crop", "count": "12 Products"},
                {"name": "Pant", "image": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?q=80&w=200&auto=format&fit=crop", "count": "23 Products"},
                {"name": "Baggy Pant", "image": "https://images.unsplash.com/photo-1628036987140-5e589e4722de?q=80&w=200&auto=format&fit=crop", "count": "7 Products"}
            ],
            "outlets": [
                {"name": "Outlet 1", "address": "X Block, Halishahar, Chattogram", "phone": "+88018123456"},
                {"name": "Outlet 2", "address": "GEC, Chattogram", "phone": "+88018123456"}
            ],
            "footer_text": f"© 2026 {shop_name}. All rights reserved."
        }
    }
    
    if db:
        try:
            db.collection("shops").document(shop_id).set(shop_data)
            add_demo_products(shop_id)
            send_json_response(handler, 201, {"message": "Shop created successfully", "shop": shop_data})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        mock_db["shops"].append(shop_data)
        add_demo_products(shop_id)
        send_json_response(handler, 201, {"message": "Mock Shop created.", "shop": shop_data})

def get_shops(handler):
    if db:
        try:
            shops_ref = db.collection("shops")
            docs = shops_ref.stream()
            shops = [doc.to_dict() for doc in docs]
            send_json_response(handler, 200, {"shops": shops})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        send_json_response(handler, 200, {"shops": mock_db["shops"]})

def update_shop(handler, shop_id):
    body = parse_request_body(handler)
    
    if db:
        try:
            shop_ref = db.collection("shops").document(shop_id)
            shop_doc = shop_ref.get()
            if not shop_doc.exists:
                send_json_response(handler, 404, {"error": "Shop not found"})
                return
            
            shop_data = shop_doc.to_dict()
            shop_data.update(body) 
            shop_ref.set(shop_data)
            send_json_response(handler, 200, {"message": "Shop updated", "shop": shop_data})
        except Exception as e:
            send_json_response(handler, 500, {"error": str(e)})
    else:
        for shop in mock_db["shops"]:
            if shop["id"] == shop_id:
                # Merge settings deeply if needed, but a simple update works for now
                shop.update(body)
                send_json_response(handler, 200, {"message": "Shop updated", "shop": shop})
                return
        send_json_response(handler, 404, {"error": "Shop not found"})

def get_shop_by_subdomain(subdomain):
    if db:
        shops_ref = db.collection("shops")
        query = shops_ref.where("subdomain", "==", subdomain).limit(1)
        docs = query.stream()
        for doc in docs:
            return doc.to_dict()
        return None
    else:
        for shop in mock_db["shops"]:
            if shop["subdomain"] == subdomain:
                return shop
        return None
