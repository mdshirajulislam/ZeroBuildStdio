from http.server import HTTPServer
from routes import AppRouter

# --- Update by Niladri Arpita for testing branch flow ---

PORT = 8000

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, AppRouter)
    print(f"Starting SaaS Server on http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        httpd.server_close()
        print("Server stopped.")

if __name__ == '__main__':
    run_server()
