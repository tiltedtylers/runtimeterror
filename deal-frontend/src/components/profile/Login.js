import React, { useState } from "react";
import { Button, FormGroup, FormControl, FormLabel, Form } from "react-bootstrap";
import "./login.css";
import axios from 'axios';

const Login = ({loginAuth}) => {

  // Holds fields sent to webtier 
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [dbConnection, setDBConnection] = useState("text-danger");

  // Changes between signup and login form
  const [isLogin, setIsLogin] = useState(true);

  // Called when user clicks signup or login button
  const handleSubmit = (event) => {
    event.preventDefault();
    let postRoute = isLogin ? "login" : "signup";
    axios.post("http://localhost:8090/" + postRoute, {
      username: username,
      password: password
    }).then(() =>{
      handleClose();
      loginAuth();
    }).catch(() => {
      alert("Login unsuccessful!");
    })

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

  // Handles visibility of login modal
  const [show, setShow] = useState(true);
  const handleClose = () => setShow(false);
  // const handleShow = () => setShow(true);

  return (
    <div>

      <Modal animation={false} backdrop="static" show={show}>
        <Modal.Header>
          <Modal.Title>RuntimeTerror - <span style={{cursor: "pointer"}} onClick={() => setIsLogin(!isLogin)}>{isLogin ? "User Login" : "User Signup"}</span></Modal.Title>
        </Modal.Header>
        <Form onSubmit={handleSubmit}>
        <Modal.Body>
        <p>The premier source of all deal information.</p>
            <FormGroup controlId="email">
              <FormLabel>Email</FormLabel>
              <FormControl
                autoFocus
                type="text"
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

          <p className={dbConnection} onClick={setDBConnection}>Database succession successful</p>
        </Modal.Body>
        <Modal.Footer>
          {isLogin ? <Button type="submit" variant="secondary">Login</Button> : <Button type="submit" variant="primary">Sign Up</Button>}
        </Modal.Footer>
        </Form>
      </Modal>

    </div>
  );

}

export default Login;
