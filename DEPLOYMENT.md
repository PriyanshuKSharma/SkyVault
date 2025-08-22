# 🚀 Deployment Guide

This guide covers various deployment options for SkyVault.

## 📋 Prerequisites

- Git repository on GitHub
- Python 3.8+ installed locally
- Docker (optional, for containerized deployment)

## 🌐 Deployment Options

### 1. Heroku (Recommended for beginners)

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-skyvault-app
   ```

4. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set FLASK_ENV=production
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

### 2. Railway

1. **Connect GitHub repository**
   - Go to [Railway.app](https://railway.app)
   - Connect your GitHub account
   - Select SkyVault repository

2. **Configure environment variables**
   ```
   SECRET_KEY=your-secret-key-here
   FLASK_ENV=production
   ```

3. **Deploy automatically** - Railway will deploy on every push to main branch

### 3. Vercel (Serverless)

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel --prod
   ```

### 4. Docker Deployment

1. **Build image**
   ```bash
   docker build -t skyvault .
   ```

2. **Run container**
   ```bash
   docker run -p 5000:5000 -e SECRET_KEY=your-secret-key skyvault
   ```

3. **Using Docker Compose**
   ```bash
   docker-compose up -d
   ```

### 5. VPS/Cloud Server

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/SkyVault.git
   cd SkyVault
   ```

2. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your values
   ```

4. **Run with Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5000 app:app
   ```

## 🔧 Environment Variables

Required environment variables for production:

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | `your-secret-key-here` |
| `FLASK_ENV` | Flask environment | `production` |
| `UPLOAD_FOLDER` | Upload directory | `uploads` |
| `ENCRYPTED_FOLDER` | Encrypted files directory | `encrypted_files` |

## 🔒 Security Considerations

- Always use a strong `SECRET_KEY` in production
- Enable HTTPS in production
- Set `FLASK_ENV=production`
- Use environment variables for sensitive data
- Regularly update dependencies

## 📊 Monitoring

- Check application logs regularly
- Monitor disk space (for file uploads)
- Set up health checks
- Monitor memory usage

## 🆘 Troubleshooting

### Common Issues

1. **Port binding errors**
   - Ensure the port is not already in use
   - Check firewall settings

2. **File permission errors**
   - Ensure upload directories exist
   - Check write permissions

3. **Environment variable issues**
   - Verify all required variables are set
   - Check variable names and values

### Getting Help

- Check the logs first
- Review this deployment guide
- Open an issue on GitHub
- Check the troubleshooting section in README

## 🎉 Success!

Once deployed, your SkyVault instance should be accessible at your deployment URL. Test the following:

- [ ] Homepage loads correctly
- [ ] User registration works
- [ ] File upload functionality
- [ ] File download works
- [ ] Authentication system
- [ ] Responsive design on mobile

Happy deploying! 🚀