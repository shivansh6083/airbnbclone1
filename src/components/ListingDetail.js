import React, { useState, useEffect } from 'react';
     import axios from 'axios';
     import { useParams } from 'react-router-dom';

     const ListingDetail = () => {
       const { id } = useParams();
       const [listing, setListing] = useState(null);

       useEffect(() => {
         const fetchListing = async () => {
           try {
             const response = await axios.get(`http://localhost:8000/api/listings/${id}/`);
             setListing(response.data);
           } catch (error) {
             console.error('Error fetching listing:', error);
           }
         };
         fetchListing();
       }, [id]);

       if (!listing) return <div className="container mx-auto p-4">Loading...</div>;

       return (
         <div className="container mx-auto p-4">
           <div className="bg-white rounded-lg shadow p-6">
             <img src={listing.image_urls || 'https://via.placeholder.com/600'} alt={listing.title} className="w-full h-96 object-cover rounded-lg mb-4" />
             <h1 className="text-2xl font-bold mb-2">{listing.title}</h1>
             <p className="text-gray-600 mb-2">{listing.location} - {listing.address}</p>
             <p className="text-gray-800 font-bold mb-2">${listing.price_per_night} / night ({listing.currency})</p>
             <p className="text-gray-600 mb-2">Rating: {listing.ratings} ({listing.reviews} reviews)</p>
             <p className="text-gray-600 mb-4">{listing.description}</p>
             <h2 className="text-xl font-semibold mb-2">Amenities</h2>
             <p className="text-gray-600 mb-4">{listing.amenities}</p>
             <h2 className="text-xl font-semibold mb-2">Host</h2>
             <p className="text-gray-600 mb-4">{listing.host_info}</p>
             <h2 className="text-xl font-semibold mb-2">Property Type</h2>
             <p className="text-gray-600">{listing.property_type}</p>
           </div>
         </div>
       );
     };

     export default ListingDetail;
     