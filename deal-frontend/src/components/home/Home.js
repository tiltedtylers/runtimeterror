import React from 'react'
import { Alert } from 'react-bootstrap';
import Login from '../profile/Login';


const Home = () => {
    return (
        <div>
            {/* <Login></Login> */}
            <p>Home</p>
            <Alert variant="dark">
                Does bootstrap work? Let's find out!
            </Alert>
        </div>
    )
}

export default Home;