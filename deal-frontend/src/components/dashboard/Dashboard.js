import React from 'react'
import { Table } from 'react-bootstrap';
import Login from '../profile/Login';

const Dashboard = ({ setAuth }) => {
    return (
        <div>
            <Login setAuth={setAuth}></Login>
            {<Table>

            </Table>}
        </div>
    )
}

export default Dashboard;