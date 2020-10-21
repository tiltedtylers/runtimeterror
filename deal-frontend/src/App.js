import React from 'react';
import logo from './logo.svg';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import Home from './components/home/Home'
import Login from './components/profile/Login'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Signup from './components/profile/Signup'

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route exact path='/login' component={Login} />
          <Route exact path='/signup' component={Signup} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
