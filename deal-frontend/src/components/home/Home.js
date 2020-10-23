import React from 'react'
import { Alert } from 'react-bootstrap';
import Login from '../profile/Login';
import CheckDbConnection from './CheckDBConnection'
// import { Alert } from 'react-bootstrap';
// import Login from '../profile/Login';


const Home = () => {
    return (
        <div>
            <p>Home</p>
            <Login />
            <Alert>
                <CheckDbConnection />
            </Alert>
            
        </div>
    )
}

export default Home;