import random
import string
from datetime import datetime


class EmailGenerator:
    @staticmethod
    def generate_unique_email():
        timestamp = str(int(datetime.now().timestamp()))
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"test_{timestamp}_{random_chars}@ya.com"


class APIHelpers:
    @staticmethod
    def prepare_ad_update_data(original_ad, updates):
        return {
            "id": original_ad['id'],
            "price": updates.get('price', original_ad['price']),
            "name": updates.get('name', original_ad['name']),
            "category": updates.get('category', original_ad['category']),
            "condition": updates.get('condition', original_ad['condition']),
            "city": updates.get('city', original_ad['city']),
            "description": updates.get('description', original_ad['description']),
            "img1": original_ad.get('img1'),
            "img2": original_ad.get('img2'),
            "img3": original_ad.get('img3'),
            "isFavorite": original_ad.get('isFavorite'),
            "owner": original_ad['owner'],
            "createdAt": original_ad['createdAt'],
            "updatedAt": original_ad['updatedAt']
        }
