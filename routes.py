from http.server import BaseHTTPRequestHandler
import os
from controllers.shop_controller import create_shop, get_shops, update_shop, get_shop_by_subdomain
from controllers.product_controller import create_product, get_products
from utils.response_util import send_json_response
from storefront_renderer import render_storefront

def serve_static_file(handler, filepath, content_type):
    if os.path.exists(filepath):
        handler.send_response(200)
        handler.send_header('Content-type', content_type)
        handler.end_headers()
        with open(filepath, 'rb') as f:
            handler.wfile.write(f.read())
    else:
        send_json_response(handler, 404, {"error": "File Not Found"})

class AppRouter(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            from dashboard_renderer import get_dashboard_html
            html = get_dashboard_html()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path.startswith('/s/'):
            # e.g., /s/myshop
            subdomain = self.path.split('/s/')[1].split('/')[0]
            shop = get_shop_by_subdomain(subdomain)
            if shop:
                from controllers.product_controller import get_products_for_shop
                products = get_products_for_shop(shop.get("id"))
                html = render_storefront(shop, products)
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))
            else:
                send_json_response(self, 404, {"error": "Store not found"})
        elif self.path.startswith('/api/shops'):
            get_shops(self)
        elif self.path.startswith('/api/products'):
            get_products(self)
        else:
            send_json_response(self, 404, {"error": "Not Found"})

    def do_POST(self):
        if self.path == '/api/shops':
            create_shop(self)
        elif self.path == '/api/products':
            create_product(self)
        else:
            send_json_response(self, 404, {"error": "Not Found"})
            
    def do_PUT(self):
        if self.path.startswith('/api/shops/'):
            shop_id = self.path.split('/api/shops/')[1]
            update_shop(self, shop_id)
        elif self.path.startswith('/api/products/'):
            product_id = self.path.split('/api/products/')[1]
            from controllers.product_controller import update_product
            update_product(self, product_id)
        else:
            send_json_response(self, 404, {"error": "Not Found"})

    def do_DELETE(self):
        if self.path.startswith('/api/products/'):
            product_id = self.path.split('/api/products/')[1]
            from controllers.product_controller import delete_product
            delete_product(self, product_id)
        else:
            send_json_response(self, 404, {"error": "Not Found"})
