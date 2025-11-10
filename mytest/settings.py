from pathlib import Path

# 📁 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent


# ⚙️ إعدادات التطوير (⚠️ غير مناسبة للإنتاج)
SECRET_KEY = 'django-insecure-y9ix#$fnds-w%nijgi()csi_!=ttb08ws*1*59*&0w%41u)ss('
DEBUG = True
ALLOWED_HOSTS = []


# 🧩 تعريف التطبيقات
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🧩 التطبيقات المخصصة للمشروع
    'accounts',   # إدارة المستخدمين والتوثيق
    'store',      # المتجر والمنتجات والسلة والطلبات
    'core',       # الصفحات العامة والمنطق المشترك
]


# 🧱 الطبقات الوسيطة (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # لدعم اللغات المتعددة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 📍 ملف عناوين المشروع (URLs)
ROOT_URLCONF = 'mytest.urls'


# 🎨 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 📂 مجلد القوالب الرئيسي
        'DIRS': [BASE_DIR / 'templates'],
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


# 🗃️ إعدادات قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 إعدادات تحقق كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 الإعدادات الدولية (اللغة والمنطقة الزمنية)
LANGUAGE_CODE = 'ar'          # اللغة الافتراضية: العربية
TIME_ZONE = 'Asia/Riyadh'     # المنطقة الزمنية: الرياض
USE_I18N = True               # تفعيل الترجمة
USE_TZ = True                 # استخدام التوقيت الزمني العالمي


# 📦 إعدادات الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # أثناء التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'    # أثناء النشر بالأمر collectstatic


# 🖼️ إعدادات ملفات الوسائط (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ⚙️ الإعداد الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 👤 تعريف نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.User'


# 🛒 إعداد السلة (Session-Based Cart)
CART_SESSION_ID = 'cart'


# 🧠 إعدادات إضافية اختيارية (تحسينات التطوير)
# عرض رسائل الأخطاء باللغة العربية
LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]

# 🔒 إعداد CSRF و Session Cookie
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
