import React, { useState } from 'react';
import axios from 'axios';

const AddSpend = () => {
    const [category, setCategory] = useState('');
    const [amount, setAmount] = useState('');
    const [currency, setCurrency] = useState('');
    const [date, setDate] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        if (!category || !amount || !currency || !date) {
            setError('All fields are required.');
            return;
        }

        try {
            await axios.post('/api/spends', { category, amount, currency, date });
            // Clear the form
            setCategory('');
            setAmount('');
            setCurrency('');
            setDate('');
        } catch (err) {
            setError('Failed to add spending entry. Please try again.');
        }
    };

    return (
        <div>
            <h2>Add New Spend</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Category:</label>
                    <input
                        type="text"
                        value={category}
                        onChange={(e) => setCategory(e.target.value)}
                    />
                </div>
                <div>
                    <label>Amount:</label>
                    <input
                        type="number"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                    />
                </div>
                <div>
                    <label>Currency:</label>
                    <input
                        type="text"
                        value={currency}
                        onChange={(e) => setCurrency(e.target.value)}
                    />
                </div>
                <div>
                    <label>Date:</label>
                    <input
                        type="date"
                        value={date}
                        onChange={(e) => setDate(e.target.value)}
                    />
                </div>
                <button type="submit">Add Spend</button>
            </form>
        </div>
    );
};

export default AddSpend;