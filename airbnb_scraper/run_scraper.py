import os
import sys
import django
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Add the airbnb_backend directory to sys.path
backend_dir = os.path.join(project_root, 'airbnb_backend')
sys.path.append(backend_dir)

# Verify the path
print(f"Project root added to sys.path: {project_root}")
print(f"Backend dir added to sys.path: {backend_dir}")
print(f"Current sys.path: {sys.path}")

# Set the correct Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnb_backend.settings')
django.setup()

# Start the Scrapy crawler process
process = CrawlerProcess(get_project_settings())
process.crawl('airbnb_spider')
process.start()  # Blocking call