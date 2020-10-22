import React from 'react'
import { Navbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
			<Navbar bg="primary" variant="dark">
				<Link to="/">
					<Navbar.Brand href="#home">RuntimeTerror</Navbar.Brand>
				</Link>
				
				<Nav className="mr-auto">
					<Link style={{ textDecoration: 'none' }} to="/">
						<Nav.Link href="#home">Home</Nav.Link>
					</Link>
					<Link style={{ textDecoration: 'none' }} to="/dashboard">
						<Nav.Link href="#home">Dashboard</Nav.Link>
					</Link>
					{/* <Link style={{ textDecoration: 'none' }} to="/login">
						<Nav.Link href="#home">Login</Nav.Link>
					</Link>
					<Link style={{ textDecoration: 'none' }} to="/signup">
						<Nav.Link href="#home">Signup</Nav.Link>
					</Link> */}
					
				</Nav>
				{/* <Form inline>
					<FormControl type="text" placeholder="Search" className="mr-sm-2" />
					<Button variant="outline-light">Search</Button>
				</Form> */}
			</Navbar>
    )
}

export default Header;
