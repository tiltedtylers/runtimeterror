import React from 'react'
import { Navbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { LinkContainer } from 'react-router-bootstrap';

const Header = () => {
    return (
		<Navbar bg="primary" variant="dark">
			<LinkContainer to="/">
				<Navbar.Brand>RuntimeTerror</Navbar.Brand>
			</LinkContainer> 
			
			<Nav className="mr-auto">
				<Nav.Link as={Link} to="/dashboard">Dashboard</Nav.Link>
				{/* <Nav.Link as={Link} to="/login">Login</Nav.Link> */}
			</Nav>
		</Navbar>
    )
}

export default Header;
