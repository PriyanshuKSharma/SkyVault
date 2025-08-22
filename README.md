# 🌟 SkyVault - Secure Personal Cloud Storage

<div align="center">
  <img src="static/icons/image-icon.png" alt="SkyVault Logo" width="100" height="100">
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
  [![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
</div>

## 📋 Overview

SkyVault is a modern, secure personal cloud storage system built with Flask. It provides military-grade encryption for your files with an intuitive, glassmorphism-inspired user interface.

### ✨ Key Features

- 🔐 **End-to-End Encryption** - Files encrypted with Fernet symmetric encryption
- 🎨 **Modern UI/UX** - Glassmorphism design with smooth animations
- 📱 **Responsive Design** - Works seamlessly on all devices
- 🚀 **Drag & Drop Upload** - Intuitive file upload experience
- 👤 **User Authentication** - Secure login with password hashing
- 🐳 **Docker Support** - Easy deployment with containerization
- 📊 **File Management** - View, download, and delete files securely

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SkyVault.git
   cd SkyVault
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 🐳 Docker Deployment

### Using Docker

```bash
# Build the image
docker build -t skyvault .

# Run the container
docker run -p 5000:5000 skyvault
```

### Using Docker Compose

```bash
docker-compose up
```

## 📁 Project Structure

```
SkyVault/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── .gitignore           # Git ignore rules
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── files.html       # File management
│   ├── login.html       # Login page
│   ├── signup.html      # Registration page
│   ├── upload.html      # File upload
│   ├── 404.html         # Error page
│   └── 500.html         # Error page
├── static/              # Static assets
│   ├── css/
│   │   └── styles.css   # Custom styles
│   └── icons/           # Application icons
├── uploads/             # Temporary uploads (gitignored)
└── encrypted_files/     # Encrypted storage (gitignored)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
UPLOAD_FOLDER=uploads
ENCRYPTED_FOLDER=encrypted_files
```

## 🎨 UI Features

- **Glassmorphism Design** - Modern transparent cards with backdrop blur
- **Smooth Animations** - CSS transitions and keyframe animations
- **Interactive Elements** - Drag & drop, hover effects, loading states
- **Responsive Layout** - Mobile-first design approach
- **Dark Theme** - Elegant gradient backgrounds

## 🔒 Security Features

- **File Encryption** - All files encrypted using Fernet symmetric encryption
- **Password Hashing** - Secure password storage with bcrypt
- **Session Management** - Flask-Login for secure user sessions
- **Input Validation** - Server-side validation for all inputs

## 🚀 Deployment Options

### GitHub Pages (Static Demo)
- Fork this repository
- Enable GitHub Pages in repository settings
- Access via `https://yourusername.github.io/SkyVault`

### Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

### Railway
```bash
# Connect your GitHub repository to Railway
# Deploy with one click
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** - Micro web framework
- **Bootstrap** - UI components and responsive design
- **Bootstrap Icons** - Beautiful icon library
- **Cryptography** - File encryption capabilities

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Check the documentation
- Contact the maintainers

---

<div align="center">
  Made with ❤️ by [Your Name]
  
  ⭐ Star this repository if you found it helpful!
</div>