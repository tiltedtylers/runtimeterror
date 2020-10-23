import React, { useState } from "react";
import { Form, Button, Card } from "react-bootstrap";

const AvgBuySell = () => {
  const [date, setDate] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    // Format YYYY-MM-DD
    console.log(date);

    // Post to something

    return 0;
  };

  return (
    <div>
      <Card>
        <Card.Body>
          <h1>Ending Position</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group>
              <Form.Label>Date</Form.Label>
              <Form.Control
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
              ></Form.Control>
            </Form.Group>
            <Form.Group>
              <Button type="submit" variant="primary">
                Submit
              </Button>
            </Form.Group>
          </Form>

          {/* Stuff to be displayed from form can be put here */}
        </Card.Body>
      </Card>
    </div>
  );
};

export default AvgBuySell;
