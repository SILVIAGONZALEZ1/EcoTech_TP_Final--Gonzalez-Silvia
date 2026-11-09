from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "clave-local-no-usar-en-produccion"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]
ROOT_URLCONF = "ejercicio_3_auditoria_web.urls"
INSTALLED_APPS = []
MIDDLEWARE = []
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
