import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './Home'
import About from './About'
import Contect from './Contect'
import Service from './Service'

// Define the Nav component
function Nav() {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">Navbar</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link active" aria-current="page" to='/home'>Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to='/about'>About</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to='/contect'>Contect</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to='/service'>Service</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

// Render the application
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter> 
    <Nav/>
    <Routes>
      <Route path='/home' element={<Home/>} />
      <Route path='/about' element={<About/>} />
      <Route path='/service' element={<Service/>} />
      <Route path='/contect' element={<Contect/>} />
    </Routes>
  </BrowserRouter>
);
