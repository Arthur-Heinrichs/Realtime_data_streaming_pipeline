import random
import uuid
from datetime import datetime, timezone
import json

EVENT_TYPES = ["view_product", "add_to_cart", "purchase", "refund"]
LOYALTY_TIERS = ["none", "bronze", "silver", "gold", "platinum"]
PAYMENT_METHODS = ["credit_card", "pix", "debit_card", "boleto", "apple_pay"]
REFUND_REASONS = [
    "customer_changed_mind",
    "defective_product",
    "late_delivery",
    "payment_issue",
]
CATEGORIES = {
    "electronics": ["smartphones", "laptops", "headphones"],
    "fashion": ["mens_clothing", "womens_clothing", "shoes"],
    "home_appliances": ["kitchen", "furniture"]
}

PLATFORMS = ["web", "mobile_app", "mobile_web"]

STATE_CITIES = {
    "SP": ["São Paulo", "Campinas", "Guarulhos", "São Bernardo do Campo", "Santo André"],
    "RJ": ["Rio de Janeiro", "Niterói", "São Gonçalo", "Duque de Caxias", "Nova Iguaçu"],
    "MG": ["Belo Horizonte", "Uberlândia", "Contagem", "Juiz de Fora", "Betim"],
    "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista", "Camaçari", "Itabuna"],
    "PR": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Canoas", "Pelotas", "Santa Maria"],
    "PE": ["Recife", "Jaboatão dos Guararapes", "Olinda", "Caruaru", "Petrolina"],
    "CE": ["Fortaleza", "Caucaia", "Juazeiro do Norte", "Maracanaú", "Sobral"],
    "SC": ["Florianópolis", "Joinville", "Blumenau", "São José", "Chapecó"],
    "GO": ["Goiânia", "Aparecida de Goiânia", "Anápolis", "Rio Verde", "Luziânia"]
}

def generate_user():
    state = random.choice(list(STATE_CITIES.keys()))
    city = random.choice(STATE_CITIES[state])
    return {
        "user_id": f"u_{random.randint(1000, 9999)}",
        "signup_date": f"2025-11-10",
        "loyalty_tier": random.choices(
            LOYALTY_TIERS,
            weights=[50, 20, 15, 10, 5]
        )[0],
        "location": {
            "country": "BR",
            "state": state,
            "city": city
        }
    }

def generate_platform():
    platform = random.choices(PLATFORMS, weights=[25,70,5])

    if platform == "web":
        brand =  random.choice(["Dell", "Lenovo", "HP", "Apple"])
        if brand == "Apple":
            return {
                "platform": "web",
                "device": {
                    "device_type": "desktop",
                    "brand": "apple",
                    "os": "macOS"
                },
                "browser": {
                    "name": "Safari",
                    "version": "122.0"
                }
            }
        else:
           return {
                "platform": "web",
                "device": {
                    "device_type": "desktop",
                    "brand": brand,
                    "os": random.choices(["Linux", "Windows"], weights=[10, 90])
                },
                "browser": {
                    "name": random.choice(["Chrome", "Firefox", "Opera"]),
                    "version": "122.0"
                }
            }
    if platform == "mobile_web":
        brand = random.choice(["Samsung", "Xiaomi", "Apple"])
        if brand == "Apple":
            return {
                "platform": "mobile_web",
                "device": {
                    "device_type": "mobile",
                    "brand": brand,
                    "os": "iOS"
                },
                "browser": {
                    "name": "Safari",
                    "version": "122.0"
                }
            }
        else:
            return {
                "platform": "mobile_web",
                "device": {
                    "device_type": "mobile",
                    "brand": random.choice(["Samsung", "Xiaomi"]),
                    "os": "Android"
                },
                "browser": {
                    "name": "Chrome",
                    "version": "122.0"
                }
            }
    # mobile_app
    else:
        brand = random.choice(["Apple", "Samsung", "Xiaomi"])
        if brand == "Apple":
            return {
                "platform": "mobile_app",
                "device": {
                    "device_type": "mobile",
                    "brand": brand,
                    "os": "iOS"
                },
                "app": {
                    "app_version": "5.4.0"
                }
            }
        else:
            return {
                "platform": "mobile_app",
                "device": {
                    "device_type": "mobile",
                    "brand": random.choice(["Xiaomi", "Samsung"]),
                    "os": "Android"
                },
                "app": {
                    "app_version": "5.4.0"
                }
            }

def generate_product():
    category = random.choice(list(CATEGORIES.keys()))
    subcategory = random.choice(CATEGORIES[category])

    return {
        "product_id": f"p_{random.randint(100, 999)}",
        "category": category,
        "subcategory": subcategory,
        "price": round(random.uniform(50, 5000), 2),
        "currency": "BRL"
    }
def generate_event():
    event_type = random.choices(EVENT_TYPES, weights=[65,20,10,5])
    timestamp = datetime.now(timezone.utc).isoformat()
    product = generate_product() 
    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "event_timestamp": timestamp,
        "user": generate_user(),
        "session": generate_platform(),
        "product": product
    }

    if event_type == "add_to_cart":
        quantity = random.randint(1, 3)
        event["cart"] = {
            "quantity": random.randint(1, 3),
            "cart_value": round(product["price"] * quantity, 2)
        }

    if event_type == "purchase":
        event["transaction"] = {
            "payment_method": random.choice(PAYMENT_METHODS),
            "installments": random.choice([1, 3, 6, 10]),
            "discount_amount": round(random.uniform(0, 300), 2)
        }


    if event_type == "refund":
        event["refund"] = {
            "original_event_id": "evt_9f8a7c",
            "refund_reason": random.choice(REFUND_REASONS),
            "refund_amount": event["product"]["price"],
            "refund_method": "credit_card"
        }
    return event

if __name__ == "__main__":
    for _ in range(3):
        print(json.dumps(generate_event(), indent=2))



# user_location_country = ['BR']
# user_location_state = ['SP', 'RJ', 'MG', 'RS', 'BA', 'PR']
# user_location_city = ['Sao Paulo', 'Rio de Janeiro','Belo Horizonte','Porto Alegre','Salvador', 'Curitiba']
# session_device_device_type = ["mobile", "desktop", "tablet"]
# session_device_brand = ["Apple","Samsung", "Motorola","Xiaomi","Dell","Lenovo","HP"]
# session_device_os =["ios", "android", "windows", "macos", "linux"]
# session_traffic_source_source = ["google", "facebook", "instagram", "tiktok", "linkedin", "email", "direct", "affiliate"]
# session_traffic_source_medium = ["cpc","organic","social","email","referral","display","push"]
# session_traffic_source_campaign = ["black_friday_2026","summer_sale","brand_awareness_q1","retargeting_campaign","launch_new_product","none"]
# product_category = ["electronics","fashion","home_appliances","sports","beauty","books"]
# product_subcategory = ["laptops","headphones","gaming_consoles","mens_clothing","womens_clothing","shoes","accessories","kitchen","furniture","decor"]
# product_currency = ["BRL", "USD", "EUR"]
# payment_method = ["credit_card","debit_card","pix","boleto","paypal","apple_pay","google_pay"]
# plataform = ["web","mobile_app","mobile_web","tablet_app"]