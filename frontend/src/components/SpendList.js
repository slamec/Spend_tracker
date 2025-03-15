import React, { useEffect, useState } from 'react';
import { fetchSpends } from '../services/api';

const SpendList = () => {
  const [spends, setSpends] = useState([]);

  useEffect(() => {
    fetchSpends()
      .then(response => {
        setSpends(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h2>Spend List</h2>
      <ul>
        {spends.map(spend => (
          <li key={spend.id}>
            {spend.category}: {spend.amount} {spend.currency} on {spend.date}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SpendList;