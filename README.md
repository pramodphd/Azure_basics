# 🚀 Azure Web App Deployment using GitHub (Python App)

## 📌 Project Overview

This project demonstrates how to deploy a Python web application to **Azure App Service** using **GitHub** and **GitHub Actions (CI/CD)**.

---

## 🧰 Technologies Used

* Python
* Git & GitHub
* Azure App Service
* GitHub Actions (CI/CD)

---

## 📁 Project Structure

```
azure-webapp-demo/
│
├── app.py
├── requirements.txt
└── .github/
    └── workflows/
        └── azure-webapps.yml
```

---

## ⚙️ Step 1: Initialize Git Repository

```bash
cd azure-webapp-demo
git init
git add .
git commit -m "Initial commit"
```

---

## 🔗 Step 2: Connect to GitHub Repository

```bash
git remote add origin https://github.com/<your-username>/Azure_basics.git
git branch -M main
git push -u origin main
```

---

## ⚠️ Common Issue Faced

### ❌ Error:

```
! [rejected] main -> main (fetch first)
```

### 📌 Reason:

Remote repository had changes (like README or workflow) not present locally.

### ✅ Fix:

```bash
git pull origin main --rebase
git push origin main
```

---

## 🔄 Daily Workflow (After Setup)

Whenever you update code:

```bash
git add .
git commit -m "Updated code"
git pull --rebase
git push origin main
```

---

## ☁️ Step 3: Create Azure Web App

1. Go to Azure Portal
2. Search → **App Services**
3. Click **Create**

### Fill details:

* Subscription: Your subscription
* Resource Group: Create or select
* Name: `your-app-name` (must be unique)
* Runtime: Python (e.g., Python 3.10)
* Region: Choose nearest

Click **Review + Create → Create**

---

## 🔗 Step 4: Connect GitHub to Azure

1. Open your **App Service**
2. Go to **Deployment Center**
3. Select:

   * Source: GitHub
   * Repository: `Azure_basics`
   * Branch: `main`
4. Click **Save**

---

## ⚙️ Step 5: GitHub Actions Workflow

Azure automatically creates a workflow file:

```
.github/workflows/azure-webapps.yml
```

### Purpose:

* Automates deployment
* Runs every time you push code

---

## 🚀 Step 6: Deployment Process

After pushing code:

```bash
git push origin main
```

### What happens:

1. GitHub Actions triggers
2. Workflow runs
3. Code is deployed to Azure
4. App becomes live

---

## 🔍 Step 7: Monitor Deployment

1. Go to GitHub repo
2. Click **Actions tab**
3. Check workflow status:

   * ✅ Success → App deployed
   * ❌ Failed → Check logs

---

## 🌐 Step 8: Access the Web App

Open in browser:

```
https://<your-app-name>.azurewebsites.net
```

---

## ⚠️ Common Errors

### ❌ DNS_PROBE_FINISHED_NXDOMAIN

**Reason:**

* App not created
* Wrong URL
* Deployment not completed

**Fix:**

* Verify app name
* Wait for deployment to complete

---

## 🧠 Key Learnings

* Git push alone does NOT deploy app
* CI/CD (GitHub Actions) automates deployment
* Azure Deployment Center links GitHub to Azure
* `git pull --rebase` avoids conflicts

---

## 📌 Conclusion

This project demonstrates a complete DevOps flow:

**Local Code → GitHub → GitHub Actions → Azure Deployment → Live Web App**

---

##  Author

Pramod
