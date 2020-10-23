import React, { useState } from "react";
import {
  Button,
  FormGroup,
  FormControl,
  FormLabel,
  Form,
} from "react-bootstrap";
import "./login.css";
import axios from "axios";

export default function Signup({ history }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const validateForm = () => {
    return username.length > 0 && password.length > 0;
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(username, password);
    axios
      .get(
        `http://localhost:8090/login?username=${username}&password=${password}`
      )
      .then((res) => {
        console.log(res.data);
        if (res.data.toString() === "true") {
          console.log("aasd");
          return history.push("/dashboard");
        } else {
          setError("Invalid Credentials");
        }
      });
  };

  return (
    <div className="main">
      <h1>Signup</h1>
      <Form onSubmit={handleSubmit}>
        <FormGroup controlId="email">
          <FormLabel>Email</FormLabel>
          <FormControl
            autoFocus
            type="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </FormGroup>
        <FormGroup controlId="password">
          <FormLabel>Password</FormLabel>
          <FormControl
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type="password"
          />
        </FormGroup>
        <Button block disabled={!validateForm()} type="submit">
          Signup
        </Button>
      </Form>
    </div>
  );
}
