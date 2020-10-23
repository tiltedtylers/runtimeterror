import React from 'react'
import { Col, Container, Jumbotron, Row } from 'react-bootstrap';
import Login from '../profile/Login';
import AvgBuySell from './AvgBuySell';
import OtherData from './OtherData';
import EndingPosition from './EndingPosition';

// We envisioned deal data coming from backend would be put here. 
const Dashboard = ({auth, loginAuth}) => {

    return (
        <div>
            {/* Checking if user is logged in */}
            {!auth ? <Login loginAuth={loginAuth}/> :
            <Container>
                <br></br>
                <Row>
                    <Col>
                        <Jumbotron>
                            <h1>Deal Dashboard</h1>
                            <p>View information on average buy/sell price, ending position, realised profit, and effective profit here. </p>
                        </Jumbotron>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <AvgBuySell></AvgBuySell>
                    </Col>
                </Row>
                <br></br>
                <Row>
                    <Col>
                        <EndingPosition></EndingPosition>
                    </Col>
                </Row>
                <br></br>
                {/* <Row>
                    <Col>
                        <OtherData></OtherData>
                    </Col>
                </Row> */}
            </Container>}
        </div>
    )
}

export default Dashboard;