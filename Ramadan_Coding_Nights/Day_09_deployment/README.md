# Streamlit App deployement on Streamlit and API Deployment on Vercel

![Deployment](images/image.png)

## Getting Started with UV, Streamlit and FastAPI

### 1️⃣ Install UV

First, install UV (if not already installed):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```sh
uv --version
```

### 2️⃣ Create and Initialize the Project

```sh
uv init day-09-deployment
cd day-09-deployment
```

### 3️⃣ Install Streamlit (Dependency)

```sh
uv add streamlit fastapi[standard]
```

## 4️⃣ Activate UV Virtual Environment

For Windows:

```sh
.venv\Scripts\activate
```

For Linux/macOS:

```sh
source .venv/bin/activate
```

### 5️⃣ Run Quiz App

```sh
streamlit run streamlit.py
```
[Streamlit App Deployed Link](https://simple-app-ramadancoding-day09.streamlit.app/)

----

## Deploying a FastAPI API on Vercel

This guide will walk you through the process of deploying a **FastAPI** application on **Vercel** step by step.

---

### **Step 1: Set Up Your FastAPI App**

Create a new Python file (`api.py`) and add your FastAPI code


### **Step 2: Create `requirements.txt`**

To ensure Vercel installs the required dependencies, create a `requirements.txt` file:

```sh
echo "fastapi[standard]" > requirements.txt
```

---

### **Step 3: Create `vercel.json`**

Vercel requires a configuration file to properly deploy your FastAPI app. Create a `vercel.json` file in your project directory

---


### **Step 4: Deploy to Vercel**

### **Deploy Your App**

Vercel will provide a URL where your API is hosted.

---

### **Step 5: Test Your API**

Once deployed, you can test your API using in your browser:

[Fast API deployed Link](https://fastapi-api-deployment.vercel.app/)

---

### **Conclusion**

Congratulations! 🎉 You have successfully deployed **Streamlit** and **FastAPI** application on **Streamlit** and **Vercel** respectively. Now you can build and expand your App and API as needed!


