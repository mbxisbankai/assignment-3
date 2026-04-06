# Assignment 3

## Git setup & usage guide

### Step 1: Installing Git
- For Windows: 
```
https://git-scm.com/install/
```

- For Mac: 
```
brew install git
```
### Step 2: Configure Git (If it's your first time setting it up)

- In your terminal:

```bash
git config --global user.name "Your username"
git config --global user.email "Your email"
```

- To confirm

``` bash
git config --list
```

### Step 3: Confirm the installation

```bash
git --version
```

### Step 4: Set up SSH

- Generate your SSH key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

- Start the SSH agent

```bash
eval "$(ssh-agent -s)"
```

- Add SSH Key to Agent

```bash
ssh-add ~/.ssh/id_ed25519
```

- Copy the SSH Key

```bash
clip < ~/.ssh/id_ed25519.pub
```

#### Add the Key to Github

- Go to GitHub → Settings → SSH and GPG Keys
- Click New SSH Key
- Paste your key and save

### Step 5: Navigate to your assignment folder

```bash
cd path/to/your/project
```


### Step 5: Clone the repository

```bash
git clone git@github.com:mbxisbankai/assignment-3.git
```

### Step 6: Pushing code

- Connect to the repository

```bash
git remote add origin git@github.com:mbxisbankai/assignment-3.git
```

- Confirm the connection

```bash
git remote -v
```

- Add files

```bash
git add .
```

- Commit files

```bash
git commit -m "your-commit-message"
```

- Push the files

```bash
git push -u origin main
```

### Step 7: Making changes

- When making changes, follow these steps

```bash
git add .
git commit -m "your-commit-message"
git push origin main
```

### Step 8: Getting the latest changes

- To get the latest version of the repository

```bash
git pull origin main
```