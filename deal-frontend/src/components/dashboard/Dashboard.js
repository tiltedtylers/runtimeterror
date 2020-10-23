import React from 'react'
import { Col, Container, Row } from 'react-bootstrap';
import Login from '../profile/Login';
import HistoricData from './HistoricData';
import OtherData from './OtherData';
import UnderlyingData from './UnderlyingData';

// We envisioned deal data coming from backend would be put here. 
const Dashboard = ({auth, loginAuth}) => {

    return (
        <div>
            {/* Checking if user is logged in */}
            {!auth ? <Login loginAuth={loginAuth}/> :
            <Container>
                <Row>
                    <Col>
                        <HistoricData></HistoricData>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <UnderlyingData></UnderlyingData>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <OtherData></OtherData>
                    </Col>
                </Row>
            </Container>}
        </div>
    )
}

export default Dashboard;