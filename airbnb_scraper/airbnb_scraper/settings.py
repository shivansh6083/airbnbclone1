# Scrapy settings for airbnb_scraper project

BOT_NAME = 'airbnb_scraper'

SPIDER_MODULES = ['airbnb_scraper.spiders']
NEWSPIDER_MODULE = 'airbnb_scraper.spiders'

# Configure Django settings
import os
import sys

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnb_backend.settings')

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 60,
}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    # Add any custom downloader middlewares here
}

# Enable or disable extensions
EXTENSIONS = {
    # Add any Scrapy extensions here
}

# Configure item pipelines
ITEM_PIPELINES = {
    # Add any pipelines here, e.g., 'myproject.pipelines.MyPipeline': 300
}

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 16

# Configure download delay
DOWNLOAD_DELAY = 1

# Enable and configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
