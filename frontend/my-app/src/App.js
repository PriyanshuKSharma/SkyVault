import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Upload from './components/Upload';
import Display from './components/Display';
import Login from './components/Login';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsAuthenticated(true);
    }
  }, []);

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
          <Route 
            path="/upload" 
            element={isAuthenticated ? <Upload /> : <Navigate to="/login" />} 
          />
          <Route 
            path="/display" 
            element={isAuthenticated ? <Display /> : <Navigate to="/login" />} 
          />
          <Route 
            path="/" 
            element={<Navigate to={isAuthenticated ? "/upload" : "/login"} />} 
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
