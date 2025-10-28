from django.core.management.utils import get_random_secret_key

if name == "__main__":
    secret_key = get_random_secret_key()
    print("Сгенерированный SECRET_KEY:")
    print(secret_key)
    print("\nДля использования в settings.py:")
    print(f"SECRET_KEY = '{secret_key}'")