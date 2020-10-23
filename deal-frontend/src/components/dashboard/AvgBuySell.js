import React, { useState } from "react";
import { Form, Button, Card } from "react-bootstrap";

const AvgBuySell = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    // Format YYYY-MM-DD
    console.log(startDate, endDate);

    // Post to something

    return 0;
  };

  return (
    <div>
      <Card>
        <Card.Body>
          <h1>Average Buy/Sell Price</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group>
              <Form.Label>Start Date</Form.Label>
              <Form.Control
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
              ></Form.Control>
            </Form.Group>
            <Form.Group>
              <Form.Label>End Date</Form.Label>
              <Form.Control
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
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
