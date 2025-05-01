import React, { useState, useEffect } from 'react';
     import axios from 'axios';
     import { Link } from 'react-router-dom';

     const SearchResults = () => {
       const [listings, setListings] = useState([]);
       const [error, setError] = useState(null);
       const [filters, setFilters] = useState({
         location: 'New York',
         checkin: '2025-06-01',
         checkout: '2025-06-07',
         guests: 2,
         minPrice: 0,
         maxPrice: 1000,
         minRating: 0,
       });

       useEffect(() => {
         fetchListings();
       }, []);

       const fetchListings = async () => {
         try {
           const response = await axios.get('http://localhost:8000/api/listings/');
           console.log('API Response:', response.data); // Debug log
           if (response.data && Array.isArray(response.data)) {
             let filteredListings = response.data.filter(listing => {
               return (
                 listing.location.toLowerCase().includes(filters.location.toLowerCase()) &&
                 listing.price_per_night >= filters.minPrice &&
                 listing.price_per_night <= filters.maxPrice &&
                 listing.ratings >= filters.minRating
               );
             });
             setListings(filteredListings);
             setError(null);
           } else {
             setError('No listings found in the response.');
           }
         } catch (error) {
           console.error('Error fetching listings:', error);
           setError('Failed to fetch listings. Please ensure the backend is running.');
         }
       };

       const handleInputChange = (e) => {
         setFilters({ ...filters, [e.target.name]: e.target.value });
       };

       const handleSearch = () => {
         fetchListings();
       };

       return (
         <div className="container mx-auto p-4">
           <div className="mb-4 flex flex-wrap gap-4">
             <input
               type="text"
               name="location"
               value={filters.location}
               onChange={handleInputChange}
               placeholder="Location"
               className="p-2 border rounded"
             />
             <input
               type="date"
               name="checkin"
               value={filters.checkin}
               onChange={handleInputChange}
               className="p-2 border rounded"
             />
             <input
               type="date"
               name="checkout"
               value={filters.checkout}
               onChange={handleInputChange}
               className="p-2 border rounded"
             />
             <input
               type="number"
               name="guests"
               value={filters.guests}
               onChange={handleInputChange}
               placeholder="Guests"
               className="p-2 border rounded"
             />
             <input
               type="number"
               name="minPrice"
               value={filters.minPrice}
               onChange={handleInputChange}
               placeholder="Min Price"
               className="p-2 border rounded"
             />
             <input
               type="number"
               name="maxPrice"
               value={filters.maxPrice}
               onChange={handleInputChange}
               placeholder="Max Price"
               className="p-2 border rounded"
             />
             <input
               type="number"
               name="minRating"
               value={filters.minRating}
               onChange={handleInputChange}
               placeholder="Min Rating"
               className="p-2 border rounded"
             />
             <button onClick={handleSearch} className="p-2 bg-pink-500 text-white rounded">Search</button>
           </div>
           {error && <p className="text-red-500 mb-4">{error}</p>}
           <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
             {listings.length > 0 ? (
               listings.map(listing => (
                 <Link to={`/listing/${listing.id}`} key={listing.id} className="bg-white rounded-lg shadow overflow-hidden">
                   <img src={listing.image_urls || 'https://via.placeholder.com/300'} alt={listing.title} className="w-full h-48 object-cover" />
                   <div className="p-4">
                     <h2 className="text-lg font-semibold">{listing.title}</h2>
                     <p className="text-gray-600">{listing.location}</p>
                     <p className="text-gray-800 font-bold">${listing.price_per_night} / night</p>
                     <p className="text-gray-600">Rating: {listing.ratings} ({listing.reviews} reviews)</p>
                   </div>
                 </Link>
               ))
             ) : (
               <p className="text-gray-600">No listings found. Try adjusting your filters or ensure the backend has data.</p>
             )}
           </div>
         </div>
       );
     };

     export default SearchResults;