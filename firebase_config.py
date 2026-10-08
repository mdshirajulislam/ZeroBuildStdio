import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initialize_firebase():
    cred_path = "serviceAccountKey.json"
    
    if not os.path.exists(cred_path):
        print(f"WARNING: {cred_path} not found. Firebase operations will run in mock mode.")
        return None
        
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        print("Firebase initialized successfully!")
        return firestore.client()
    except Exception as e:
        print(f"Firebase initialization error: {e}")
        return None

db = initialize_firebase()

# In-memory storage for mock mode so UI actually works
mock_db = {
    "shops": [],
    "products": []
}
