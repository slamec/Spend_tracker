import React from 'react';
import AddSpend from './components/AddSpend';
import SpendList from './components/SpendList';

const App = () => {
  return (
    <div>
      <h1>Spend Tracker</h1>
      <AddSpend />
      <SpendList />
    </div>
  );
};

export default App;