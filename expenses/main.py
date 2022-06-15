from datetime import datetime
import firebase_admin
from firebase_admin import firestore
import os

# Initial firestore app, with credentials

firebase_admin.initialize_app()
db = firestore.client()

def set_expense(request):

    # Import required libraries
    from datetime import datetime
    import random

    # Add new document to collection
    try:
        ref = db.collection('expenses').document()
        ref.set({
            'created_at': datetime.now(),
            'expense': random.randint(1,200)
        })
        return 'OK', 200
    except Exception as e:
        return e, 400


