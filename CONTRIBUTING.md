# Contributing to SkyVault

Thank you for your interest in contributing to SkyVault! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Basic knowledge of Flask and web development

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/SkyVault.git
   cd SkyVault
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

## 🧪 Testing

Before submitting a pull request:
- Test your changes locally
- Ensure the application starts without errors
- Test file upload/download functionality
- Verify responsive design on different screen sizes

## 📋 Pull Request Process

1. **Update documentation** if needed
2. **Add/update tests** for new features
3. **Ensure code follows style guidelines**
4. **Create descriptive commit messages**
5. **Submit pull request** with detailed description

### Commit Message Format
```
type(scope): description

Examples:
feat(ui): add drag and drop file upload
fix(auth): resolve login validation issue
docs(readme): update installation instructions
```

## 🐛 Bug Reports

When reporting bugs, please include:
- Operating system and version
- Python version
- Browser (if UI related)
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

## 💡 Feature Requests

For new features:
- Check existing issues first
- Provide clear use case
- Explain expected behavior
- Consider implementation complexity

## 🔒 Security

- Never commit sensitive data
- Use environment variables for secrets
- Follow security best practices
- Report security issues privately

## 📞 Questions?

- Open an issue for discussion
- Check existing documentation
- Review closed issues for similar questions

Thank you for contributing to SkyVault! 🌟