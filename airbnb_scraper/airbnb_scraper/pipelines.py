from airbnb_backend.listings.models import Listing


class AirbnbScraperPipeline:
    def process_item(self, item, spider):
        Listing.objects.create(
            title=item.get('title', 'N/A'),
            location=item.get('location', 'N/A'),
            address=item.get('address', 'N/A'),
            price_per_night=item.get('price_per_night', 0.0),
            currency=item.get('currency', 'USD'),
            total_price=item.get('total_price'),
            image_urls=item.get('image_urls', ''),
            ratings=item.get('ratings', 0.0),
            description=item.get('description', 'N/A'),
            reviews=item.get('reviews', 0),
            amenities=item.get('amenities', ''),
            host_info=item.get('host_info', 'N/A'),
            property_type=item.get('property_type', 'Apartment'),
        )
        return item