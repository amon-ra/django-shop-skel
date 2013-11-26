# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
# Django settings for cyc project.
from django.utils.translation import ugettext as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_NAME= "web"

ADMINS = (
    ('amon-ra', 'amon.raj@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, PROJECT_NAME, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'u%ury_4u!)86$1*^(ho&i^*c%+fi+#ri07(4o3yc5he9*#+j_^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware', #Activate on debugging
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

ROOT_URLCONF = PROJECT_NAME+'.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = PROJECT_NAME+'.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
    os.path.join(PROJECT_PATH, PROJECT_NAME, "templates"),
)

INSTALLED_APPS = (
    'gunicorn',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'templateaddons',
    'djangocms_text_ckeditor', # note this needs to be above the 'cms' entry
    'cms',
    'cms.stacks',
    'djangocms_admin_style',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'cms.plugins.file',
    #'cms.plugins.text',    
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    #'cms.plugins.link',
    #'cms.plugins.picture',
    'cms.plugins.snippet',
    #'cms.plugins.teaser',
    #'cms.plugins.video',  
    'cms.plugins.inherit',
    'cmsplugin_embeddedmenu',
    'cmsplugin_htmlsitemap',
    'mptt',
    'filer',
    'easy_thumbnails',    
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',    
    'cmsplugin_filer_link',
    'cmsplugin_filer_utils',  
    'cmsplugin_filer_gallery',
    'discount',
    'discount.default_discounts',
    'polymorphic',
    'configurableproduct',
    'shop',
    'shop.addressmodel',
    'treeadmin',
    'shop_categories',  
    'shop_simplevariations',
    'paypal.standard.ipn',
    'shop_paypal',
    #'shop_example',
    'cmsplugin_shopcart',
    'cmsplugin_topproducts',
    'cmsplugin_featuredproducts',    
    'cmsplugin_userorders',
    PROJECT_NAME+'.addonsCYC',
    'menus',
    'south',
    'sekizai', 
    'reversion',
    'imagestore',
    'sorl.thumbnail',
    'imagestore.imagestore_cms',
    'tagging',
    #'cmsplugin_gallery', #replaced by imagestore
    #'cms_themes', Fault PageAddForm (cms.admin.forms) no v3 compatible
    'zinnia',
    'cmsplugin_zinnia',
    #Debugging
    "debug_toolbar",
    "django_extensions",
    

)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
        
CKEDITOR_SETTINGS = {
        'language': '{{ language }}',
        'toolbar': 'CMS',
        'skin': 'moono'
    }

ENABLE_CPRODUCT_ADMIN = True
#SHOP_PRODUCT_MODEL = ('shop_example.models.product.Product','shop_example')
#SHOP_ADDRESS_MODEL = ('shop_example.models.address.Address','shop_example')
#SHOP_CATEGORIES_CATEGORY_MODEL = ('shop_example.models.category.Category','shop_example')
SHOP_PAYMENT_BACKENDS = (
    'shop.payment.backends.pay_on_delivery.PayOnDeliveryBackend',
    'shop_paypal.offsite_paypal.OffsitePaypalBackend',
)
SHOP_SHIPPING_BACKENDS = (
    'shop.shipping.backends.flat_rate.FlatRateShipping',
)
SHOP_SHIPPING_FLAT_RATE = "10.00"
SHOP_CART_MODIFIERS = [
        'shop.cart.modifiers.tax_modifiers.TenPercentGlobalTaxModifier',
        'shop.cart.modifiers.rebate_modifiers.BulkRebateModifier',
        'shop_simplevariations.cart_modifier.ProductOptionsModifier',
        'shop_simplevariations.cart_modifier.TextOptionsModifier',
        'discount.cart_modifiers.DiscountCartModifier',
        ]

PAYPAL_RECEIVER_EMAIL = 'amon.raj@gmail.com'
PAYPAL_CURRENCY_CODE = 'es'
#PAYPAL_LC

LANGUAGES = [
    ('es','Spanish'),('en', 'English'),
]

##Per site language configuration
#CMS_LANGUAGES = {
    #1: [
        #{
            #'code': 'en',
            #'name': gettext('English'),
            #'fallbacks': ['de', 'fr'],
            #'public': True,
            #'hide_untranslated': True,
            #'redirect_on_fallback':False,
        #},
        #{
            #'code': 'de',
            #'name': gettext('Deutsch'),
            #'fallbacks': ['en', 'fr'],
            #'public': True,
        #},
        #{
            #'code': 'fr',
            #'name': gettext('French'),
            #'public': False,
        #},
    #],
    #2: [
        #{
            #'code': 'nl',
            #'name': gettext('Dutch'),
            #'public': True,
            #'fallbacks': ['en'],
        #},
    #],
    #'default': {
        #'fallbacks': ['en', 'de', 'fr'],
        #'redirect_on_fallback':True,
        #'public': True,
        #'hide_untranslated': False,
    #}
#}
CMS_TEMPLATES = (
    #('page.html',_('Base Page')),  
    (os.path.join('acuvi','page.html'),_('Acuvi Base')),
    (os.path.join('acuvi','banner3col.html'),_('Acuvi (Banner and 3 Cols)')),
    (os.path.join('acuvi','index.html'),_('Acuvi Index')),
)

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError:
    pass
