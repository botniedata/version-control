*This README.md file was generated on 20240211 by Botnie Data*
<!-- remove all comments (like this) before final save  -->

### General Information
---

### Version Control and Modular Environment to Python
---

### Author Information:
 - Creator: Botnie Data
 - Inspired: Josh Dev
 - Community: Data Engineer Pilipinas
---

### What is Version Control?
<p>Version control, or source control, tracks software code changes using tools to help teams manage and monitor modifications efficiently.</p>

---

### What is Modular Environment?
<p>Creates a modular environment in Pyhton using a built-in `venv` module. It sets up a  virtual environment for a project. Virtual environment isolate project dependencies, making it easier to manage and avoid conflicts between different projects</p>

---
# Requirements
|   No      |   Software                          |   Link                                       |
|-----------|-------------------------------------|----------------------------------------------|
|   1       |   Git                               |   `https://git-scm.com/downloads`            |
|   2       |   VSCode                            |   `https://code.visualstudio.com/download`   |
|   3       |   Python                            |   `https://www.python.org/downloads/`        |

---

### Create a directory to initialize your Git Repository Locally
|   Step    |   Code                          |   Action                                        |   Tool/Software  |   Message
|-----------|---------------------------------|-------------------------------------------------|------------------|-------------------------------
|   1       |   `mkdir <repository-name>`     |   creates your repository for Git               |   command prompt |
|   2       |   `cd <repository-name>`        |   change directory on created repository        |   command prompt |
|   3       |   `git init .`                  |   creates git repository inside the directory   |   command prompt |   Initialized empty Git. repository in <directory> with .git
|   4       |   `code .`                      |   open vscode via terminal                      |   command prompt |

### Initialize the created repository
|   Step    |   Code                          |   Action                                        |   Tool/Software  |   Message
|-----------|---------------------------------|-------------------------------------------------|------------------|-------------------------------
|   1       |                                 |   open terminal press ``` CTRL + ` ```          |   vscode editor  |    Pointed to the created respository directory
|   2       |   `new-item README.md`          |   creates README.md file                        |   vscode editor  |    README.md file an introductory file for everyone
|           |                                 |   add message `this is my first README.md`      |   vscode editor  |    **U** means modification added to a file
|   3       |   `git add README.md`           |   adds README.md file to git repository         |   vscode editor  |    **A** means new file added to the repository ready to commit
|   4       |   `git commit -m "message"`     |   commits README file                           |   vscode editor  |    `"message"` adds action or activity done
|           |                                 |                                                 |   vscode editor  |    [master (root-commit) *hash*] added READEME
|   5       |   `git log`                     |   checks the activities                         |   vscode editor  |    commit *hash* (HEAD -> master) ...

### Create a GitHub Repository
|   Step    |   Code                          |   Action                                           |   Tool/Software  |   Message
|-----------|---------------------------------|----------------------------------------------------|------------------|-------------------------------
|   1       |                                 |   go to `https://github.com/signup`                |   GitHub Website |    Create your GitHub Account
|   2       |                                 |   go to `https://github.com/dashboard` Press `NEW` |   GitHub Website |    Create your GitHub Repository
|           |                                 |   `https://github.com/new`                         |   GitHub Website |    Name your GitHub Repository
|           |                                 |   `Description` (optional)                         |   GitHub Website |    Add some description of your repository
|           |                                 |   set as `Public`                                  |   GitHub Website |    `Anyone on the internet can see this repository`
|           |                                 |   set as `Public`                                  |   GitHub Website |    `Anyone on the internet can see this repository`
|           |                                 |   unchecked ` Add a README file`                   |   GitHub Website |    README.md file already created via VSCode
|           |                                 |   add `.gitignore` set as `None`                   |   GitHub Website |    No `.gitignore` file has been created
|           |                                 |   add `License` set as `None`                      |   GitHub Website |    No `License` file has been created
|           |                                 |   press `Create repository` button                 |   GitHub Website |    Generate a GitHub Respository

### Generating a new SSH key
<p> SSH Keys used for secure authentication between local machine to our GitHub Account. It enables a secure wat to establish identity when interacting with GitHub repositories. </p><br>
Link: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent <br>
Note: Follow the instructions provided by GitHub Docs [Steps 2. (Open Git Bash) to 7. (Add the SSH public key to your account on GitHub)]

---

### Adding a new SSH key to your GitHub account
<p> Adding SSH key to your GitHub Account, you enable a secure and convenient way to authenticate yourself when interacting with GitHub repositories </p><br>
- Cloning repositories (git clone)
- Pushing Changes (git push)
- Pulling updates (git pull)
Link: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

---

### Create connection between Repositories (Git Local Repository and GitHub Repositories)
|   Step    |   Code                                                                   |   Action                                        |   Tool/Software  |   Message
|-----------|--------------------------------------------------------------------------|-------------------------------------------------|------------------|-------------------------------
|   1       |   `git remote add origin git@github.com:<username>/<repository>.git`     |   create a remote connections between two repos |   VSCode         |                                
|   2       |   `git branch -M main`                                                   |   create a main branch                          |   VSCode         |        
|   3       |   `git push -u origin main`                                              |   sends local files to GitHub repository        |   VSCode         |       
|           |   Message prompts: Enumerating objects: n, done. Counting objects ... branch 'main' set up to track 'origin/main'.                            |
|           |   Check now your GitHub repositor for the file that sends via `git push`                                                                      |


