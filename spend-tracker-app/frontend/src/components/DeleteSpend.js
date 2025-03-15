import React, { useState } from 'react';
import axios from 'axios';

const DeleteSpend = ({ spendId, onDelete }) => {
    const [confirm, setConfirm] = useState(false);

    const handleDelete = async () => {
        try {
            await axios.delete(`http://localhost:5000/spends/${spendId}`);
            onDelete(spendId);
        } catch (error) {
            console.error("Error deleting spend:", error);
        }
    };

    return (
        <div>
            {confirm ? (
                <div>
                    <p>Are you sure you want to delete this spend?</p>
                    <button onClick={handleDelete}>Yes</button>
                    <button onClick={() => setConfirm(false)}>No</button>
                </div>
            ) : (
                <button onClick={() => setConfirm(true)}>Delete Spend</button>
            )}
        </div>
    );
};

export default DeleteSpend;