import React from 'react';
import logo from './logo.svg';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import Home from './components/home/Home'
import Dashboard from './components/dashboard/Dashboard';
import Header from './components/layout/Header'

import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Header></Header>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route exact path="/dashboard" component={Dashboard}></Route>
        </Switch>
      </Router>
      
    </div>
  );
}

export default App;
