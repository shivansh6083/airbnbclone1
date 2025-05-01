import scrapy
from scrapingbee import ScrapingBeeClient
from airbnb_backend.listings.models import Listing


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb_spider'
    start_urls = ['https://www.airbnb.com/s/New-York/homes?checkin=2025-06-01&checkout=2025-06-07&adults=2']

    def __init__(self):
        self.client = ScrapingBeeClient(api_key='05TMX3C8OHOFA1C4PCZHK6EIFTQHZJOA9J3E4DKUVF4VIXRO1RYBONUBG0842DR4T8152GJ6DYE5HTX4')

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, meta={'handle_httpstatus_all': True})

    def parse(self, response):
        if response.status == 200:
            listings = response.xpath('//div[contains(@data-testid, "listing-card")]')
            for listing in listings:
                item = {
                    'title': listing.xpath('.//div[contains(@data-testid, "listing-card-title")]/text()').get(default='N/A').strip(),
                    'location': listing.xpath('.//div[contains(@data-testid, "listing-card-subtitle")]/text()').get(default='N/A').strip(),
                    'address': listing.xpath('.//div[contains(@data-testid, "listing-card-name")]/text()').get(default='N/A').strip(),
                    'price_per_night': listing.xpath('.//span[contains(@class, "_tyxjp1")]/text()').get(default='0').strip().replace('$', '').replace(',', ''),
                    'currency': 'USD',
                    'total_price': None,
                    'image_urls': listing.xpath('.//img/@src').get(default=''),
                    'ratings': listing.xpath('.//span[contains(@data-testid, "review-rating")]/text()').get(default='0').strip().replace('★', ''),
                    'description': 'N/A',
                    'reviews': listing.xpath('.//span[contains(@data-testid, "review-count")]/text()').get(default='0').strip().replace(' reviews', ''),
                    'amenities': ','.join(listing.xpath('.//div[contains(@data-testid, "amenities")]/span/text()').getall()),
                    'host_info': listing.xpath('.//div[contains(@data-testid, "host-info")]/text()').get(default='N/A').strip(),
                    'property_type': listing.xpath('.//div[contains(@data-testid, "listing-card-type")]/text()').get(default='Apartment').strip(),
                }
                try:
                    item['price_per_night'] = float(item['price_per_night']) if item['price_per_night'] else 0.0
                    item['ratings'] = float(item['ratings']) if item['ratings'] else 0.0
                    item['reviews'] = int(item['reviews']) if item['reviews'] else 0
                    self.save_to_db(item)
                    yield item
                except Exception as e:
                    self.logger.error(f"Error processing item: {e}")
        else:
            self.logger.error(f"Failed to fetch page: {response.status}")

    def save_to_db(self, item):
        try:
            Listing.objects.update_or_create(
                title=item['title'],
                defaults={
                    'location': item['location'],
                    'address': item['address'],
                    'price_per_night': item['price_per_night'],
                    'currency': item['currency'],
                    'total_price': item['total_price'],
                    'image_urls': item['image_urls'],
                    'ratings': item['ratings'],
                    'description': item['description'],
                    'reviews': item['reviews'],
                    'amenities': item['amenities'],
                    'host_info': item['host_info'],
                    'property_type': item['property_type'],
                }
            )
            self.logger.info(f"Saved listing: {item['title']}")
        except Exception as e:
            self.logger.error(f"Error saving to DB: {e}")