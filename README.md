# **SkyVault - Personal Cloud Storage**

SkyVault is a secure personal cloud storage system built using Flask. The application allows users to upload files, which are then encrypted before storage, ensuring privacy and security. Users can log in, upload, view, download, and delete their encrypted files securely.

---

## **Project Structure**

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
├── Dockerfile                # Docker configuration for building the application image
├── .gitlab-ci.yml            # Implemented pipeline
├── docker-compose.yml        # Docker Compose configuration file
└── README.md                 # Project documentation
```

---

## **Installation**

### **Using Python**

### **Prerequisites**

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### **Steps to Setup**

1. Clone the repository:

   ```bash
   git clone https://github.com/PriyanshuKSharma/SkyVault.git
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

## **Using Docker**

### **Prerequisites**

Ensure that Docker and Docker Compose are installed on your system.

### **Steps to Setup**

1. Clone the repository:

   ```bash
   git clone https://github.com/PriyanshuKSharma/SkyVault.git
   cd SkyVault
   ```

2. Build the Docker image:

   ```bash
   docker build -t priyanshuksharma/skyvault-cloud:1.0 .
   ```

3. Run the application using Docker:

   ```bash
   docker run -p 5000:5000 priyanshuksharma/skyvault-cloud:1.0
   ```

   The app will be available at `http://127.0.0.1:5000/`.

4. Alternatively, use Docker Compose to set up and run the application:

   ```bash
   docker-compose up
   ```

---

## **Pushing to Docker Hub**

If you want to share your Docker image, you can push it to Docker Hub:

1. Tag the Docker image:

   ```bash
   docker tag skyvault-cloud:1.0 priyanshuksharma/skyvault-cloud:1.0
   ```

2. Push the image to Docker Hub:

   ```bash
   docker push priyanshuksharma/skyvault-cloud:1.0
   ```

Your image will now be available on Docker Hub at `https://hub.docker.com/repository/docker/priyanshuksharma/skyvault-cloud`.

---

## **Features**

- **User Authentication**: Secure login functionality with password hashing.
- **File Uploads**: Users can upload files which are automatically encrypted using `Fernet` encryption.
- **File Management**: Users can view, download, and delete their uploaded files securely.
- **Error Handling**: Custom error pages for 404 (not found) and 500 (server error).
- **Secure Storage**: All uploaded files are stored in the `encrypted_files/` directory.

---

## **How to Use**

1. **Login**: Access the login page at `/login` and enter your credentials.
2. **Upload Files**: After logging in, navigate to the homepage to upload files. The files will be encrypted before storage.
3. **View Files**: After uploading files, you can view all your uploaded files on the `/files` page.
4. **Download Files**: You can download your encrypted files from the `/download/<filename>` route.
5. **Delete Files**: Delete any uploaded file from the `/delete/<filename>` route.

---

## **File Encryption**

Uploaded files are encrypted using the `cryptography` package with `Fernet` symmetric encryption. The encrypted files are stored in the `encrypted_files/` directory, ensuring that the files are only accessible to authenticated users.

---

## **Error Pages**

- **404.html**: Custom page shown when a route or file is not found.
- **500.html**: Custom page shown for internal server errors.

---

## **Future Enhancements**

- **Multiple User Support**: Add functionality to allow multiple users with separate storage spaces.
- **File Sharing**: Enable sharing of files between users or publicly.
- **More Secure Authentication**: Implement additional authentication features, like multi-factor authentication (MFA).
- **File Compression**: Add a feature for compressing large files before uploading them.

---

## Running the Docker Image on Another System  

If you want to run the SkyVault application on another system using Docker, follow these steps:  

### **1. Save the Docker Image**  
On your system, save the Docker image to a tar file:  

```bash  
docker save -o skyvault-cloud.tar priyanshuksharma/skyvault-cloud:1.0  
```  

This will create a file named `skyvault-cloud.tar` that contains your Docker image.  

---  

### **2. Transfer the Docker Image**  
Copy the `skyvault-cloud.tar` file to the target system. You can use a USB drive, file-sharing services, SCP, or any preferred method.  

---  

### **3. Load the Docker Image**  
On the target system, load the Docker image from the tar file:  

```bash  
docker load -i skyvault-cloud.tar  
```  

After loading, verify that the image is available:  

```bash  
docker images  
```  

You should see the image listed (e.g., `priyanshuksharma/skyvault-cloud:1.0`).  

---  

### **4. Run the Docker Image**  
Start the container using:  

```bash  
docker run -p 5000:5000 priyanshuksharma/skyvault-cloud:1.0  
```  

This maps port `5000` on the local system to port `5000` in the container. Open a browser and access the application at:  

```
http://127.0.0.1:5000  
```  

---  

### **Alternative: Use [Docker Hub](https://hub.docker.com/r/priyanshuksharma/skyvault-cloud)**  
If the target system has internet access, you can pull the image directly from Docker Hub:  

1. Log in to Docker Hub (if necessary):  
   ```bash  
   docker login  
   ```  

2. Pull the image:  
   ```bash  
   docker pull priyanshuksharma/skyvault-cloud:1.0  
   ```  

3. Run the container:  
   ```bash  
   docker run -p 5000:5000 priyanshuksharma/skyvault-cloud:1.0  
   ```  

---

### **Note**  
- Ensure Docker is installed on the target system.  
- Replace `1.0` with the appropriate version tag if needed.  

---

## **License**

This project is not licensed.

---

## **Acknowledgments**

- Flask: A micro web framework used to build the web application.
- Cryptography: Provides secure file encryption and decryption using `Fernet` symmetric encryption.
- Bcrypt: Used for securely hashing passwords.
- Docker: Simplified application deployment with containerization.

---
