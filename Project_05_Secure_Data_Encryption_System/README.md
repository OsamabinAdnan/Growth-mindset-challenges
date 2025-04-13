# Secure Data Encryption System

A robust web application built with Streamlit that provides secure data encryption and user authentication.

## 🔐 Features

- **Secure User Authentication**
  - Password-based key derivation using PBKDF2-HMAC-SHA256
  - Account lockout after 3 failed attempts
  - Unique salt per user
  - Session management

- **Strong Encryption**
  - AES-256-CBC encryption
  - Fernet symmetric encryption
  - Secure key management
  - PKCS7 padding

- **User Dashboard**
  - Account statistics
  - Data encryption metrics
  - Security status monitoring
  - Recent activity tracking

- **Data Management**
  - Secure data storage
  - Encrypted data retrieval
  - JSON-based persistence
  - Activity logging

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Encryption**: cryptography.fernet
- **Key Derivation**: PBKDF2-HMAC-SHA256
- **Data Storage**: JSON
- **Security Features**:
  - 100,000 PBKDF2 iterations
  - 16-byte random salts
  - 256-bit encryption keys

## 📋 Requirements

```text
streamlit
cryptography
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/OsamabinAdnan/Growth-mindset-challenges.git
cd Project_05_Secure_Data_Encryption_System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

## 💻 Usage

1. **Registration**
   - Create a new account with username and password
   - System generates secure encryption keys

2. **Login**
   - Enter credentials
   - Account locks after 3 failed attempts
   - 60-second lockout period

3. **Data Encryption**
   - Enter text in the "Store Data" section
   - Data is encrypted using AES-256
   - Encrypted data stored securely

4. **Data Retrieval**
   - Access encrypted data from dashboard
   - Decrypt data using stored keys
   - View decrypted content securely

## 🔒 Security Features

1. **Key Derivation (PBKDF2)**
   - SHA256 hash function
   - 100,000 iterations
   - 32-byte key length
   - Unique salt per user

2. **Encryption (Fernet)**
   - AES-256-CBC encryption
   - PKCS7 padding
   - Authenticated encryption
   - Timestamp-based token expiry

3. **User Protection**
   - Account lockout system
   - Failed attempt tracking
   - Session management
   - Secure password storage

## ⚠️ Security Considerations

- Keys are derived using cryptographic best practices
- All data is encrypted at rest
- User sessions are managed securely
- Protection against brute force attacks

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📺 Live Demo

[Secure Data Encryption]()

## 👨‍💻 Author

**Osama bin Adnan**
- GitHub: [@OsamaBinAdnan](https://github.com/OsamaBinAdnan)
- LinkedIn: [Osama bin Adnan](https://www.linkedin.com/in/osama-bin-adnan/)
- Twitter: [@OsamaBinAdnan](https://x.com/osamabinadnan1)
- YouTube: [@ainertia](https://youtube.com/@ainertia/)

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Python Cryptography library maintainers
- The open-source community