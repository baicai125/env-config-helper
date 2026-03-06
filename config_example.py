import os

def load_config():
    config = {
        "api_key": os.getenv("API_KEY"),
        "db_host": os.getenv("DB_HOST"),
        "db_password": os.getenv("DB_PASSWORD")
    }
    return config

if __name__ == "__main__":
    config = load_config()
    print("Configuration loaded:", config)
