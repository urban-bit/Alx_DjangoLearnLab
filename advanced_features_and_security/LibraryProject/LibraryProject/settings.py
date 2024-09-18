from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'  # Replace this with a secure key


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Turn off debug in production

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']  # Add your production domain(s)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # Add CSP middleware for Content Security Policy
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.x/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.x/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.x/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.x/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.x/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Security settings to enforce HTTPS and improve security
# Enforce HTTPS for all connections
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # Enable HSTS for 1 year (in seconds)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains in the HSTS policy
SECURE_HSTS_PRELOAD = True  # Enable HSTS preloading

# Only send session and CSRF cookies over HTTPS
SESSION_COOKIE_SECURE = True  # Secure session cookies
CSRF_COOKIE_SECURE = True  # Secure CSRF cookies

# Prevent the browser from MIME-sniffing the content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser’s XSS filter to help prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent your site from being framed to protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Set Content Security Policy (CSP) headers to reduce XSS risks
CSP_DEFAULT_SRC = ("'self'",)  # Only allow scripts, styles, and content from your domain
CSP_SCRIPT_SRC = ("'self'",)  # Restrict JavaScript to the same domain
CSP_STYLE_SRC = ("'self'",)  # Restrict stylesheets to the same domain

# Secure proxy header if using a reverse proxy like Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Add your production domain(s)
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Debugging setting (ensure DEBUG is False in production)
DEBUG = False  # Turn off debugging mode in production