import React from 'react';
     import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
     import SearchResults from './components/SearchResults';
     import ListingDetail from './components/ListingDetail';

     function App() {
       return (
         <Router>
           <div className="min-h-screen bg-gray-100">
             <nav className="bg-white shadow p-4">
               <Link to="/" className="text-xl font-bold text-pink-500">Airbnb Clone</Link>
             </nav>
             <Routes>
               <Route path="/" element={<SearchResults />} />
               <Route path="/listing/:id" element={<ListingDetail />} />
             </Routes>
           </div>
         </Router>
       );
     }

     export default App;