import React, { useEffect, useState } from 'react';
import { fetchSpends } from '../services/api';

const SpendList = () => {
    const [spends, setSpends] = useState([]);

    useEffect(() => {
        const getSpends = async () => {
            const data = await fetchSpends();
            setSpends(data);
        };

        getSpends();
    }, []);

    return (
        <div>
            <h2>Spending List</h2>
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Amount</th>
                        <th>Currency</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {spends.map((spend) => (
                        <tr key={spend.id}>
                            <td>{spend.category}</td>
                            <td>{spend.amount}</td>
                            <td>{spend.currency}</td>
                            <td>{spend.date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default SpendList;