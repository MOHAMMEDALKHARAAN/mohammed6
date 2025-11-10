from pathlib import Path

# 📁 بناء المسارات داخل المشروع
BASE_DIR = Path(__file__).resolve().parent.parent


# ⚙️ إعدادات سريعة للتطوير (غير مناسبة للإنتاج)
SECRET_KEY = 'django-insecure-y9ix#$fnds-w%nijgi()csi_!=ttb08ws*1*59*&0w%41u)ss('
DEBUG = True
ALLOWED_HOSTS = []


# 🧩 تعريف التطبيقات
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات المخصصة للمشروع
    'accounts',   # إدارة المستخدمين والتوثيق
    'store',      # المتجر والمنتجات والطلبات
    'core',       # الصفحات العامة والمنطق المشترك
]


# 🧱 الطبقات الوسيطة (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # لدعم اللغات
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 📍 ملف إعدادات عناوين المشروع
ROOT_URLCONF = 'mytest.urls'


# 🎨 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب العام
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


# 🚀 إعدادات WSGI
WSGI_APPLICATION = 'mytest.wsgi.application'


# 🗃️ قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 الإعدادات الدولية (اللغة والموقع)
LANGUAGE_CODE = 'ar'          # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'     # المنطقة الزمنية: الرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True


# 📦 الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


# 🖼️ ملفات الوسائط (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ⚙️ الحقول الافتراضية للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 👤 استخدام نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.User'
