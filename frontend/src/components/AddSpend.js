import React, { useState } from 'react';
import { addSpend } from '../services/api'; // Corrected import path

const AddSpend = () => {
  const [formData, setFormData] = useState({
    db_name: 'spend',
    table_name: 'spends',
    category: '',
    amount: '',
    currency: '',
    date: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await addSpend(formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="category" value={formData.category} onChange={handleChange} placeholder="Category" />
      <input type="number" name="amount" value={formData.amount} onChange={handleChange} placeholder="Amount" />
      <input type="text" name="currency" value={formData.currency} onChange={handleChange} placeholder="Currency" />
      <input type="date" name="date" value={formData.date} onChange={handleChange} placeholder="Date" />
      <button type="submit">Add Spend</button>
    </form>
  );
};

export default AddSpend;