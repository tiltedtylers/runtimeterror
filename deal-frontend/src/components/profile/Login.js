import React, { useState } from "react";
import { Button, FormGroup, FormControl, FormLabel, Form, Modal } from "react-bootstrap";
import "./login.css";

export default function Login(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [dbConnection, setDBConnection] = useState("text-danger");


  function validateForm() {
    return email.length > 0 && password.length > 0;
  }

  function handleSubmit(event) {
    event.preventDefault();
    console.log(email, password);
  }

  const [show, setShow] = useState(true);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <div>

      <Modal animation={false} backdrop="static" show={show} onHide={handleClose}>
        <Modal.Header>{/* closebutton */}
          <Modal.Title>RuntimeTerror - User Login</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <p>The premier source of all deal information.</p>
          <form onSubmit={handleSubmit}>
            <FormGroup controlId="email">
              <FormLabel>Email</FormLabel>
              <FormControl
                autoFocus
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
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
            {/* <Button block disabled={!validateForm()} type="submit">
              Login
            </Button> */}
          </form>
          {console.log(props.auth)}

          <p className={dbConnection} onClick={setDBConnection}>Database succession successful</p>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={() => handleClose()} variant="secondary">Log In</Button>
          <Button onClick={() => handleClose()} variant="primary">Sign Up</Button>
        </Modal.Footer>
      </Modal>
    </div>
  );

}