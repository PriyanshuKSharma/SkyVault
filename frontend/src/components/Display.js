import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Display() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    const fetchFiles = async () => {
      const token = localStorage.getItem('token');
      const response = await axios.get('http://localhost:5000/files', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setFiles(response.data);
    };
    fetchFiles();
  }, []);

  return (
    <div>
      <h2>Uploaded Files</h2>
      <ul>
        {files.map((file) => (
          <li key={file.id}>
            <a href={`http://localhost:5000/files/${file.id}`}>{file.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Display;
