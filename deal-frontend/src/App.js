import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import Dashboard from './components/dashboard/Dashboard';
import Header from './components/layout/Header'

import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './components/profile/Login'
import Signup from './components/profile/Signup'



const App = () => {

  const [auth, setAuth] = useState(false);

  const loginSetAuth = () => {
    setAuth(true);
  }

  const requireAuth = () => {
    if (!auth) {
      return <Login></Login>;
    }
    return <Dashboard></Dashboard>;
  }

  return (
    <div className="App">
      
      <Router>
        {/* {auth ? <Header></Header> : null} */}
        <Header></Header>
        <Switch>
          <Route exact path="/" component={requireAuth}></Route>
          {/* <Route exact path="/dashboard" component={() => requireAuth(Dashboard)} onEnter={requireAuth}></Route> */}
          <Route exact path='/login' component={Login} onEnter={requireAuth}/>
          <Route exact path='/signup' component={Signup} onEnter={requireAuth}/>
        </Switch>
      </Router>
      
    </div>
  );
}

export default App;
