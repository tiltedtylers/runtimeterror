import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "./App.css";
import Dashboard from "./components/dashboard/Dashboard";
import Header from "./components/layout/Header";
import "bootstrap/dist/css/bootstrap.min.css";
import Login from "./components/profile/Login";

const App = () => {
  const [auth, setAuth] = useState(false);

  // passing hook down to dashboard then login component to update authentication hook here
  const loginAuth = () => {
    setAuth(!auth);
  };

  return (
    <div className="App">
      <Router>
        {auth ? <Header></Header> : null}
        <Switch>
          <Route
            exact
            path="/"
            render={(props) => (
              <Dashboard {...props} auth={auth} loginAuth={loginAuth} />
            )}
          />
          <Route exact path="/login" component={Login} />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
