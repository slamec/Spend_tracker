import React, { useState, useEffect } from 'react';
import AddSpend from './components/AddSpend';
import EditSpend from './components/EditSpend';
import DeleteSpend from './components/DeleteSpend';
import SpendList from './components/SpendList';
import { fetchSpends } from './services/api';

function App() {
    const [spends, setSpends] = useState([]);
    const [selectedSpend, setSelectedSpend] = useState(null);
    const [action, setAction] = useState('add');

    useEffect(() => {
        loadSpends();
    }, []);

    const loadSpends = async () => {
        const data = await fetchSpends();
        setSpends(data);
    };

    const handleAdd = (newSpend) => {
        setSpends([...spends, newSpend]);
    };

    const handleEdit = (updatedSpend) => {
        setSpends(spends.map(spend => spend.id === updatedSpend.id ? updatedSpend : spend));
        setSelectedSpend(null);
        setAction('add');
    };

    const handleDelete = (id) => {
        setSpends(spends.filter(spend => spend.id !== id));
    };

    return (
        <div className="App">
            <h1>Spend Tracker</h1>
            <AddSpend onAdd={handleAdd} />
            {selectedSpend && (
                <EditSpend spend={selectedSpend} onEdit={handleEdit} />
            )}
            <SpendList spends={spends} onEdit={setSelectedSpend} onDelete={handleDelete} />
        </div>
    );
}

export default App;