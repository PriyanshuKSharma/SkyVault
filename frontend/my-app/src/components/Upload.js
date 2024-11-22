import React, { useState } from 'react';
import axios from 'axios';

function Upload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    const token = localStorage.getItem('token');
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      console.log(response.data);
    } catch (error) {
      console.error('File upload failed:', error);
    }
  };

  return (
    <div>
      <h2>Upload File</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default Upload;
