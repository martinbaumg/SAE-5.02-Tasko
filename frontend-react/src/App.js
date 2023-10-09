import './App.css';
import React, { Component } from 'react';
import NavBar from './components/NavBar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { eel } from './eel.js';

class App extends Component {
  constructor(props) {
    super(props);
    eel.set_host('ws://localhost:8888');
    eel.hello();
  }
  render() {
    return (
      <>
        <Router>
          <NavBar />
          <Routes>
            <Route path="/" />
          </Routes>
        </Router>
      </>
    );
  }
}

export default App;
