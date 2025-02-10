import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME", "migrador_sistec"),
        "USER": os.getenv("DATABASE_USER", "migrador"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "migrador"),
        "HOST": os.getenv("DATABASE_HOST", "localhost"),
        "PORT": os.getenv("DATABASE_PORT", "5435"),
    }
}
