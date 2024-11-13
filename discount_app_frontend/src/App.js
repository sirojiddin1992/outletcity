import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [shops, setShops] = useState([]);

  useEffect(() => {
    // Backenddan do'konlar ro'yxatini olish
    axios.get('http://127.0.0.1:5000/api/shops')
      .then(response => {
        setShops(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the shops!', error);
      });
  }, []);

  return (
    <div>
      <h1>Discount Shops</h1>
      <ul>
        {shops.map(shop => (
          <li key={shop.id}>
            <h2>{shop.name}</h2>
            <p>{shop.description}</p>
            <p>Discount: {shop.discount}%</p>
            <p>Location: {shop.location}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
