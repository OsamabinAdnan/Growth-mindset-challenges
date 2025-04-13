###########################################
# IMPORTS AND CONFIGURATION
###########################################
# Core Python imports
import streamlit as st          # Web framework for creating interactive UI
import json                     # JSON handling for data persistence
import os                       # File and directory operations
import time                     # Time-based operations and timestamps

# Cryptography-related imports
from base64 import urlsafe_b64encode  # URL-safe base64 encoding for binary data
import base64                          # Base64 encoding and decoding
from cryptography.fernet import Fernet  # Implements AES-256 in CBC mode with PKCS7 padding
from cryptography.hazmat.primitives import hashes  # Cryptographic hash functions
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # Key stretching function
from cryptography.hazmat.backends import default_backend  # Cryptographic backend operations


###########################################
# PAGE CONFIGURATION
###########################################
# Set Streamlit page configuration for better UX
st.set_page_config(
    page_title= "Secure Data Encryption",
    page_icon= "🔐"  # Lock emoji indicates security focus
)


# Set background gradient using CSS
st.markdown("""
    <style>
    .stApp {
        font-family: 'Inter', sans-serif;
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    </style>
""", unsafe_allow_html=True)



###########################################
# CONSTANTS AND INITIALIZATION
###########################################
# System-wide constants
DATA_FILE = 'data.json'        # Persistent storage file for user data and encrypted content
LOCKOUT_TIME = 60             # Duration (seconds) for account lockout after failed attempts

# Initialize data storage
# The stored_data structure:
# {
#     "username": {
#         "salt": "hex_encoded_salt",
#         "key": "derived_key_base64",
#         "data": ["encrypted_item1", "encrypted_item2", ...]
#     }
# }
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        stored_data = json.load(file)
else:
    stored_data = {}          # Initialize empty if first run

###########################################
# SESSION STATE MANAGEMENT
###########################################
# Initialize session state variables
if "user" not in st.session_state:
    st.session_state.user = None              # Current logged-in username
if "lockout" not in st.session_state:
    st.session_state.lockout = 0              # Timestamp when lockout expires
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = {}     # Track login failures per user

###########################################
# SECURITY FUNCTIONS
###########################################
def derive_key(passkey: str, salt: bytes) -> bytes:
    """
    Implements PBKDF2 (Password-Based Key Derivation Function 2) for secure key generation
    
    Technical Details:
    - Uses SHA256 as the hash function
    - Generates a 32-byte key (256 bits) suitable for AES-256
    - Performs 100,000 iterations for computational cost
    - Includes unique salt for rainbow table protection
    
    Args:
        passkey (str): User-provided password/key material
        salt (bytes): Random salt (16 bytes recommended)
    Returns:
        bytes: URL-safe base64 encoded key for Fernet encryption
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),    # SHA256 provides strong cryptographic security
        length=32,                    # 32 bytes = 256 bits for AES-256
        salt=salt,                    # Unique salt prevents precomputed attacks
        iterations=100_000,           # High iteration count slows brute-force attempts
        backend=default_backend()     # Use system's crypto backend
    )
    return urlsafe_b64encode(kdf.derive(passkey.encode()))

###########################################
# DATA PERSISTENCE
###########################################
def save_data():
    """
    Persists the current state to disk
    
    Handles:
    - User credentials
    - Encrypted data
    - Salt values
    - Derived keys
    """
    with open(DATA_FILE, 'w') as file:
        json.dump(stored_data, file)

###########################################
# USER AUTHENTICATION
###########################################
def register_user(username, password):
    """
    Register a new user with encryption key
    Args:
        username (str): New username
        password (str): User's password
    Returns:
        bool: True if registration successful, False if username exists
    """
    if username in stored_data:
        return False
    salt = os.urandom(16)                     # Generate random salt
    key = derive_key(password, salt)          # Generate encryption key
    stored_data[username] = {
        'salt': salt.hex(),                   # Store salt as hex
        'key': key.decode(),                  # Store key as string
        'data': []                            # Initialize empty data list
    }
    save_data()
    return True

def login_user(username, password):
    """
    Authenticate user login
    Args:
        username (str): Username to check
        password (str): Password to verify
    Returns:
        bool: True if credentials are valid
    """
    if username not in stored_data:
        return False
    salt = bytes.fromhex(stored_data[username]['salt'])
    key = derive_key(password, salt).decode()
    return key == stored_data[username]['key']

###########################################
# ENCRYPTION/DECRYPTION
###########################################
def encrypt_data(text, key):
    """
    Encrypt user data
    Args:
        text (str): Text to encrypt
        key (str): Encryption key
    Returns:
        str: Encrypted data as string
    """
    cipher = Fernet(key.encode())
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, key):
    """
    Decrypt user data
    Args:
        encrypted_text (str): Text to decrypt
        key (str): Decryption key
    Returns:
        str: Decrypted data as string
    """
    cipher = Fernet(key.encode())
    return cipher.decrypt(encrypted_text.encode()).decode()

###########################################
# USER INTERFACE
###########################################
# Create navigation menu in sidebar
st.sidebar.title('Secure Data Encryption System')
st.sidebar.image('images/sidebar.png', use_container_width= True)

# Create title for main page
st.title('🔐 Secure Data Encryption 🔑')

# Authentication UI - Handle user login/register
if not st.session_state.user:
    st.subheader(' Login or Register')
    auth_action = st.radio('First register yourself then login to continue', ['Login', 'Register'])
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if auth_action == 'Register':
        if st.button('Register'):
            if register_user(username, password):
                st.success('Registration successful. Please login.')
            else:
                st.error('Username already exists. Please choose a different one.')
    
    elif auth_action == 'Login':
        lockout_time = st.session_state.lockout
        current_time = time.time()
        if username in st.session_state.failed_attempts and current_time < lockout_time:
            remaining = int(lockout_time - current_time)
            st.error(f'Account locked. Please wait {remaining} seconds before trying again.')
        elif st.button('Login'):
            if login_user(username, password):
                st.session_state.user = username
                st.session_state.failed_attempts[username] = 0
                st.success('✅ Login successful!')
            else:
                st.session_state.failed_attempts[username] = st.session_state.failed_attempts.get(username, 0) + 1
                if st.session_state.failed_attempts[username] >= 3:
                    st.session_state.lockout = current_time + LOCKOUT_TIME
                    st.error('🚫 Too many failed attempts. You are temporarily locked out.')
                else:
                    st.error('❌ Invalid username or password. Please try again.')

# Main Application UI - Show after successful login
else:
    # Define available menu options
    menu = ['Dashboard', 'Store Data', 'Retrieve Data', 'Logout']
    choice = st.sidebar.selectbox('Select from below Menu', menu)

    # Get current user and their encryption key
    user = st.session_state.user
    key = stored_data[user]['key']

    # Handle different menu options
    if choice == 'Dashboard':
        # Create dashboard layout with columns
        st.header(f"🎯 Welcome to Your Dashboard, {user}")
        
        # Create three columns for metrics
        col1, col2, col3 = st.columns(3)

        # Column 1: Account Information
        with col1:
            st.subheader('👤 Account Info')
            st.info(f"""
            **Username:** {user}

            **Account Created:** {time.ctime(os.path.getctime(DATA_FILE))}

            **Last Login:** {time.strftime('%d-%m-%Y %H:%M:%S')}
            """)
        
        # Column 2: Data Statistics
        with col2:
            st.subheader('📊 Data Statistics')
            encrypt_count = len(stored_data[user]['data'])
            st.metric(
                label='Encrypted Items',
                value=encrypt_count,
                delta=f'Total Size: {sum(len(item) for item in stored_data[user]["data"])/1024:.2f} KB'
            )

        # Column 3: Security Status
        with col3:
            st.subheader('🔒 Security Status')
            failed_attempts = st.session_state.failed_attempts.get(user, 0)
            security_status = "🟢 Good" if failed_attempts == 0 else "🟡 Medium" if failed_attempts < 3 else "🔴 Critical"
            st.warning(f"""
            **Security Status:** {security_status}
            **Failed Attempts:** {failed_attempts}/3
            **Protection:** PBKDF2-SHA256
            """)

        # Recent Activity Section
        st.subheader('📝 Recent Activity')
        if encrypt_count > 0:
            with st.expander('View Recent Encrypted Data'):
                for i, encrypted in enumerate(stored_data[user]['data'][-3:], 1):
                    st.text(f"Data Count {encrypt_count-2+i}: {encrypted[:50]}...")
        else:
            st.info('No recent encrypted data.')

        # Security Tips Section
        with st.expander('🛡️ Security Tips'):
            st.markdown("""
            * **Password Security**: Use strong, unique passwords
            * **Data Protection**: All data is encrypted using AES-256
            * **Account Safety**: Account locks after 3 failed attempts
            * **Key Management**: Each user has a unique encryption key
            * **Salt Protection**: Unique salt for each password hash
            """)
        
        # Quick Action
        st.subheader("⚡ Logout")
        if st.button('🚪 Logout'):
            choice = 'Logout'
            st.session_state.user = None
            st.session_state.failed_attempts = {}
            st.session_state.lockout = 0
            st.rerun()


    
    elif choice == 'Store Data':
        # Data encryption and storage interface
        st.subheader('📂 Store Data Securely:')
        user_data = st.text_area('Enter Data to Store:')
        if st.button('Encrypt and Save'):
            st.spinner('Encrypting and saving data...')
            time.sleep(3)
            if user_data:
                # Encrypt and store the user's data
                encrypted = encrypt_data(user_data, key)
                stored_data[user]['data'].append(encrypted)
                save_data()
                st.success('Data encrypted and saved successfully.')
    
    elif choice == 'Retrieve Data':
        # Data retrieval and decryption interface
        st.subheader('🔓 Retrieve Stored Data:')
        st.write('Select a data item to decrypt:')
        for i, encrypted in enumerate(stored_data[user]['data']):
            if st.button(f"Decrypt Data {i+1}"):
                try:
                    decrypted = decrypt_data(encrypted, key)
                    st.info(f"Decrypted Data: {decrypted}")
                except Exception as e:
                    st.error(f"Error decrypting data: {e}")
    
    elif choice == 'Logout':
        # Handle user logout and reset session state
        st.session_state.user = None
        st.session_state.failed_attempts = {}
        st.session_state.lockout = 0
        st.success('👋 Logged out successfully.')


# Add horizontal line separator
st.write('---')

# Create footer with social media links using HTML/CSS
st.markdown(
    """
    <div style=" text-align: center; color: #888; font-size: 1.2em;">
        Made by <a href="/" target="_blank" style="color: #888;">Osama bin Adnan</a>
        <div style="display: flex; justify-content: center; margin-top: 10px; gap: 10px;">
            <a href='https://github.com/OsamaBinAdnan' target='_blank'>
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">    
            </a>
            <a href='https://www.linkedin.com/in/osama-bin-adnan/' target='_blank'>
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
            </a>
            <a href='https://x.com/osamabinadnan1' target='_blank'>
                <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
            </a>
            <a href='https://youtube.com/@ainertia/' target='_blank'>
                <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
            </a>
        </div>
    </div>
    """,
    # Allow HTML rendering in Streamlit
    unsafe_allow_html=True    
)