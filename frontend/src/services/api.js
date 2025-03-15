import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export const addSpend = (data) => {
  // Convert amount to integer
  data.amount = parseInt(data.amount, 10);
  return axios.post(`${API_URL}/add`, data);
};

export const updateSpend = (data) => {
  return axios.put(`${API_URL}/update`, data);
};

export const deleteSpend = (data) => {
  return axios.delete(`${API_URL}/delete`, { data });
};

export const fetchSpends = () => {
  return axios.get(`${API_URL}/spends`);
};