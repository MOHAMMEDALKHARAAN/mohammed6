from pathlib import Path

# 📁 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent


# ⚙️ إعدادات التطوير (غير مناسبة للإنتاج)
SECRET_KEY = 'django-insecure-y9ix#$fnds-w%nijgi()csi_!=ttb08ws*1*59*&0w%41u)ss('
DEBUG = True
ALLOWED_HOSTS = []


# 🧩 تعريف التطبيقات
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
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
    'django.middleware.locale.LocaleMiddleware',  # لدعم اللغات المتعددة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 📍 ملف إعداد عناوين المشروع
ROOT_URLCONF = 'mytest.urls'


# 🎨 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 🟤 مسار القوالب الرئيسي
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


# 🗃️ قاعدة البيانات (SQLite الافتراضية)
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
LANGUAGE_CODE = 'ar'          # اللغة الافتراضية: العربية
TIME_ZONE = 'Asia/Riyadh'     # المنطقة الزمنية: الرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True


# 📦 إعدادات الملفات الثابتة (Static Files)
STATIC_URL = '/static/'

# أثناء التطوير، Django سيبحث عن الملفات داخل هذا المسار
STATICFILES_DIRS = [BASE_DIR / 'static']

# أثناء النشر، يتم تجميع كل الملفات هنا بأمر collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'


# 🖼️ إعدادات ملفات الوسائط (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ⚙️ الإعداد الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 👤 تعريف نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.User'
