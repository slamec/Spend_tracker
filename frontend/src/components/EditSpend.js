import React, { useState } from 'react';
import { updateSpend } from '../services/api';

const EditSpend = () => {
  const [formData, setFormData] = useState({
    db_name: 'spend',
    table_name: 'spends',
    column_name_1: 'amount',
    value_1: '',
    column_name_2: 'category',
    value_2: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    updateSpend(formData)
      .then(response => {
        console.log(response.data);
        // Handle success
      })
      .catch(error => {
        console.error(error);
        // Handle error
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="value_2" value={formData.value_2} onChange={handleChange} placeholder="Category" />
      <input type="number" name="value_1" value={formData.value_1} onChange={handleChange} placeholder="Amount" />
      <button type="submit">Update Spend</button>
    </form>
  );
};

export default EditSpend;