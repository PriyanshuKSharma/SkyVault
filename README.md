# SkyVault - Personal Cloud Storage

SkyVault is a secure personal cloud storage system built using Flask. The application allows users to upload files, which are then encrypted before storage, ensuring privacy and security. Users can log in, upload, view, download, and delete their encrypted files securely.

---

## Project Structure

The project is organized as follows:

```
SkyVault/
├── app.py                    # Main application file
├── uploads/                  # Original uploaded files (if necessary)
├── encrypted_files/          # All encrypted files stored here
├── templates/                # HTML templates
│   ├── index.html            # Homepage with file upload form
│   ├── files.html            # Page to view uploaded files
│   ├── login.html            # Login page
│   ├── 404.html              # Custom 404 page
│   ├── 500.html              # Custom 500 error page
└── static/                   # Static files (e.g., CSS, JS)
    └── css/
        └── styles.css        # Custom styles for the web pages
    └── icons/
        └── image-icon.png
        └── pdf-icon.png
├── requirements.txt          # Python dependencies for the project
└── README.md                 # Project documentation
```

---

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Steps to Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/SkyVault.git
   cd SkyVault
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **For Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **For macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python app.py
   ```

   The app will be available at `http://127.0.0.1:5000/`.

---

## Features

- **User Authentication**: Secure login functionality with password hashing.
- **File Uploads**: Users can upload files which are automatically encrypted using `Fernet` encryption.
- **File Management**: Users can view, download, and delete their uploaded files securely.
- **Error Handling**: Custom error pages for 404 (not found) and 500 (server error).
- **Secure Storage**: All uploaded files are stored in the `encrypted_files/` directory.

---

## How to Use

1. **Login**: Access the login page at `/login` and enter your credentials.
2. **Upload Files**: After logging in, navigate to the homepage to upload files. The files will be encrypted before storage.
3. **View Files**: After uploading files, you can view all your uploaded files on the `/files` page.
4. **Download Files**: You can download your encrypted files from the `/download/<filename>` route.
5. **Delete Files**: Delete any uploaded file from the `/delete/<filename>` route.

---

## File Encryption

Uploaded files are encrypted using the `cryptography` package with `Fernet` symmetric encryption. The encrypted files are stored in the `encrypted_files/` directory, ensuring that the files are only accessible to authenticated users.

---

## Error Pages

- **404.html**: Custom page shown when a route or file is not found.
- **500.html**: Custom page shown for internal server errors.

---

## Future Enhancements

- **Multiple User Support**: Add functionality to allow multiple users with separate storage spaces.
- **File Sharing**: Enable sharing of files between users or publicly.
- **More Secure Authentication**: Implement additional authentication features, like multi-factor authentication (MFA).
- **File Compression**: Add a feature for compressing large files before uploading them.

---

## License

This project is not licensed.

---

## Acknowledgments

- Flask: A micro web framework used to build the web application.
- Cryptography: Provides secure file encryption and decryption using `Fernet` symmetric encryption.
- Bcrypt: Used for securely hashing passwords.

---
