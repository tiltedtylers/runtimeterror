import React, { useState } from "react";
import { Button, FormGroup, FormControl, FormLabel, Form } from "react-bootstrap";
import "./login.css";
import axios from 'axios'

export default function Login({history}) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null)

  function validateForm() {
    return username.length > 0 && password.length > 0;
  }

  function handleSubmit(event) {
    event.preventDefault();
    console.log(username, password);
    axios.get(`http://localhost:8090/login?username=${username}&password=${password}`).then(res => {
    console.log(res.data)
    if(res.data.toString() === "true"){
        console.log('aasd')
        return window.open("/dashboard","_self")
      }else{
        setError("Invalid Credentials")
      }
    })
  }

  return (
    <div className="main">
        <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <FormGroup controlId="username">
          <FormLabel>username</FormLabel>
          <FormControl
            autoFocus
            type="username"
            value={username}
            onChange={e => setUsername(e.target.value)}
          />
        </FormGroup>
        <FormGroup controlId="password">
          <FormLabel>Password</FormLabel>
          <FormControl
            value={password}
            onChange={e => setPassword(e.target.value)}
            type="password"
          />
        </FormGroup>
        <Button block disabled={!validateForm()} type="submit">
          Login
        </Button>
  {error && <div>{error}</div>}
      </form>
    </div>
  );
}