import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login({ setIsAuthenticated }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/auth/login', {
        username,
        password,
      });

      if (response.status === 200) {
        localStorage.setItem('token', response.data.token);
        setIsAuthenticated(true);
        navigate('/upload');
      } else {
        document.getElementById('loginMessage').innerText = response.data.message;
      }
    } catch (error) {
      console.error('Login failed:', error);
      document.getElementById('loginMessage').innerText = 'Login failed. Please try again.';
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      <div id="loginMessage" class="mt-3"></div>
    </div>
  );
}

export default Login;
