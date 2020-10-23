import React, { useState } from "react";
import {
  Button,
  FormGroup,
  FormControl,
  FormLabel,
  Form,
  Modal,
} from "react-bootstrap";
import "./login.css";
import axios from "axios";
import CheckDbConnection from "../home/CheckDBConnection";

const Login = ({ loginAuth }) => {
  // Holds fields sent to webtier
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // Changes between signup and login form
  const [isLogin, setIsLogin] = useState(true);

  // Called when user clicks signup or login button
  const handleSubmit = (event) => {
    event.preventDefault();
    // let postRoute = isLogin ? "login" : "signup";
    axios
      .post(
        `http://localhost:8090/login?username=${username}&password=${password}`
      )
      .then((res) => {
        if (res.data.toString() === "true") {
          handleClose();
          loginAuth();
        } else {
          alert("Login unsuccessful!");
        }
      })
      .catch((err) => {
        console.log("Error Found", err);
      });
  };

  // Handles visibility of login modal
  const [show, setShow] = useState(true);
  const handleClose = () => setShow(false);
  // const handleShow = () => setShow(true);

  return (
    <div>
      <Modal animation={false} backdrop="static" show={show}>
        <Modal.Header>
          <Modal.Title>
            RuntimeTerror -{" "}
            <span
              style={{ cursor: "pointer" }}
              onClick={() => setIsLogin(!isLogin)}
            >
              {isLogin ? "User Login" : "User Signup"}
            </span>
          </Modal.Title>
        </Modal.Header>
        <Form onSubmit={handleSubmit}>
          <Modal.Body>
            <p>The premier source of all deal information.</p>
            <FormGroup controlId="email">
              <FormLabel>Username</FormLabel>
              <FormControl
                autoFocus
                type="text"
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
            <CheckDbConnection />
          </Modal.Body>
          <Modal.Footer>
            {isLogin ? (
              <Button type="submit" variant="secondary">
                Login
              </Button>
            ) : (
              <Button type="submit" variant="primary">
                Sign Up
              </Button>
            )}
          </Modal.Footer>
        </Form>
      </Modal>
    </div>
  );
};

export default Login;
