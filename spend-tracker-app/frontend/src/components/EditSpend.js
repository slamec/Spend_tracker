import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';
import api from '../services/api';

const EditSpend = () => {
    const { id } = useParams();
    const history = useHistory();
    const [spendData, setSpendData] = useState({
        category: '',
        amount: '',
        currency: '',
        date: ''
    });

    useEffect(() => {
        const fetchSpendData = async () => {
            try {
                const response = await api.get(`/spends/${id}`);
                setSpendData(response.data);
            } catch (error) {
                console.error('Error fetching spend data:', error);
            }
        };

        fetchSpendData();
    }, [id]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setSpendData({ ...spendData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.put(`/spends/${id}`, spendData);
            history.push('/spend-list');
        } catch (error) {
            console.error('Error updating spend data:', error);
        }
    };

    return (
        <div>
            <h2>Edit Spend Entry</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Category:</label>
                    <input
                        type="text"
                        name="category"
                        value={spendData.category}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Amount:</label>
                    <input
                        type="number"
                        name="amount"
                        value={spendData.amount}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Currency:</label>
                    <input
                        type="text"
                        name="currency"
                        value={spendData.currency}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Date:</label>
                    <input
                        type="date"
                        name="date"
                        value={spendData.date}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit">Update Spend</button>
            </form>
        </div>
    );
};

export default EditSpend;