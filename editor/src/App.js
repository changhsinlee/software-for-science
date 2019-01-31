import React, { Component } from 'react';
import SqliteActions from './episodes/sqlite-actions';
import './App.css';

class App extends Component {
  render() {
    return (
      <SqliteActions />
    );
  }
}

export default App;
