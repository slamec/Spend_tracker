import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Adjust the URL based on your backend configuration

export const addSpend = async (spendData) => {
    try {
        const response = await axios.post(`${API_URL}/spends`, spendData);
        return response.data;
    } catch (error) {
        throw new Error('Error adding spend: ' + error.message);
    }
};

export const editSpend = async (id, spendData) => {
    try {
        const response = await axios.put(`${API_URL}/spends/${id}`, spendData);
        return response.data;
    } catch (error) {
        throw new Error('Error editing spend: ' + error.message);
    }
};

export const deleteSpend = async (id) => {
    try {
        const response = await axios.delete(`${API_URL}/spends/${id}`);
        return response.data;
    } catch (error) {
        throw new Error('Error deleting spend: ' + error.message);
    }
};

export const fetchSpends = async () => {
    try {
        const response = await axios.get(`${API_URL}/spends`);
        return response.data;
    } catch (error) {
        throw new Error('Error fetching spends: ' + error.message);
    }
};