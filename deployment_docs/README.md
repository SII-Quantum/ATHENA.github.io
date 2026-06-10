# Deployment Guide for ATHENA Website

This website is generated and deployed using GitHub Pages.

## 1. Initial Setup and Push

First, ensure you have initialized the git repository and committed all files:
```bash
cd ATHENA.github.io
git init
git add .
git commit -m "Initial commit for ATHENA website"
```

## 2. Pushing to GitHub

Add your GitHub repository as the remote origin and push the main branch:
```bash
git remote add origin https://github.com/SII-Quantum/ATHENA.github.io.git
git branch -M main
# Note: If you encounter an authentication error (like publickey or app password), 
# make sure you have your GitHub SSH keys set up or use a PAT (Personal Access Token).
git push -u origin main
```

## 3. Enable GitHub Pages

1. Navigate to your repository on GitHub (https://github.com/SII-Quantum/ATHENA.github.io).
2. Go to **Settings** (tab).
3. Scroll down or select **Pages** from the left sidebar.
4. Under "Build and deployment", set "Source" to **Deploy from a branch**.
5. Select the `main` branch and `/ (root)` folder.
6. Click **Save**.

Your website will be available at `https://SII-Quantum.github.io/ATHENA.github.io` (or similar depending on the exact repository name and user/org config) after a few minutes.
