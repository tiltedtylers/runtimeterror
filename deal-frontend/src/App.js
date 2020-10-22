import React, { useState } from 'react';
import logo from './logo.svg';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import './App.css';
import Home from './components/home/Home'
import Dashboard from './components/dashboard/Dashboard';
import Header from './components/layout/Header'

import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './components/profile/Login'
// import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Signup from './components/profile/Signup'
import { Next } from 'react-bootstrap/esm/PageItem';



const App = () => {

  const [auth, setAuth] = useState(false);

  const requireAuth = (componentName) => {
    if (!auth) {
      return (<Login auth={auth}></Login>);
    }
  }

  return (
    <div className="App">
      
      <Router>
        {/* {auth ? <Header></Header> : null} */}
        <Header></Header>
        <Switch>
          <Route exact path="/" component={() => requireAuth(Home)} onEnter={requireAuth}></Route>
          <Route exact path="/dashboard" component={() => requireAuth(Dashboard)} onEnter={requireAuth}></Route>
          <Route exact path='/login' component={Login} onEnter={requireAuth}/>
          <Route exact path='/signup' component={Signup} onEnter={requireAuth}/>
        </Switch>
      </Router>
      
    </div>
  );
}

export default App;
