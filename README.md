# Version Control and Python Virtual Environment

---

## General Information
<p>Version control ensures organized tracking of code changes, while modular environments in Python create isolated spaces for project-specific dependencies, simplifying collaboration and preventing conflicts.</p>

---

### Creator and Collaborators:
 - Created by: [Botnie Data](https://www.facebook.com/botnie.data/)
 - Inspired and Guided by: [Josh Dev](https://www.facebook.com/profile.php?id=100087019650476)
 - Data Community: [Data Engineer Pilipinas](https://www.facebook.com/DataEngineeringPilipinas)

 ---

 ### Building your First End-to-end Data Portfolio by Josh Dev
 - [Ep. 1: Introduction and Project Overview](https://www.youtube.com/watch?v=S9mVrof-bR8&t=1016s)
 - [Ep. 2: Versioning control and virtual environment essentials](https://www.youtube.com/watch?v=S9mVrof-bR8)
 - [Ep. 3: Extract data to FTP using Python](...)
 - [Ep. 4: Loading CSV files from FTP to PostgreSQL using SSIS](...)

---

### What is Version Control?
<p>Version control, or source control, tracks software code changes using tools to help teams manage and monitor modifications efficiently.</p>

---

### What is Modular Environment?
<p>Creates a modular environment in Pyhton using a built-in `venv` module. It sets up a  virtual environment for a project. Virtual environment isolate project dependencies, making it easier to manage and avoid conflicts between different projects</p>

---

# Software Requirements need to Download and install
|   No      |   Software                                         |   Link                                                                     |
|:---------:|----------------------------------------------------|----------------------------------------------------------------------------|
|   1       |   Git                                              |   `https://git-scm.com/downloads`                                          |
|           |   Git Cheat Sheet                                  |   `https://www.datacamp.com/cheat-sheet/git-cheat-sheet`                   |
|   2       |   VSCode                                           |   `https://code.visualstudio.com/download`                                 |
|   3       |   Python                                           |   `https://www.python.org/downloads/`                                      |
|   4       |   SQL Server (Developers Edition)                  |   `https://www.microsoft.com/en-us/sql-server/sql-server-downloads`        |
|           |   - Visual Studio                                  |                                                                            |
|           |   SQL Server Data Tools (SSDT for Visual Studio)   |                                                                            |
|   5       |   PostgresSQL                                      |   `https://www.postgresql.org/download/`                                   |
|   5       |   Power BI Desktop version                         |   `https://www.microsoft.com/en-us/download/details.aspx?id=58494`         |

---

### Create a directory to initialize your Git Repository Locally
|   Step    |   Code                          |   Action                                        |   Tool/Software  |   Message
|:---------:|---------------------------------|-------------------------------------------------|------------------|-------------------------------
|   1       |   `mkdir <repository-name>`     |   creates your repository for Git               |   command prompt |
|   2       |   `cd <repository-name>`        |   change directory on created repository        |   command prompt |
|   3       |   `git init .`                  |   creates git repository inside the directory   |   command prompt |   Initialized empty Git. repository in <directory> with .git
|   4       |   `code .`                      |   open vscode via terminal                      |   command prompt |

### Initialize the created repository
|   Step    |   Code                          |   Action                                        |   Tool/Software  |   Message
|:---------:|---------------------------------|-------------------------------------------------|------------------|-------------------------------
|   1       |                                 |   open terminal press ``` CTRL + ` ```          |   vscode editor  |    Pointed to the created respository directory
|   2       |   `new-item README.md`          |   creates README.md file                        |   vscode editor  |    README.md file an introductory file for everyone
|           |                                 |   add message `this is my first README.md`      |   vscode editor  |    **U** means modification added to a file
|   3       |   `git add README.md`           |   adds README.md file to git repository         |   vscode editor  |    **A** means new file added to the repository ready to commit
|   4       |   `git commit -m "message"`     |   commits README file                           |   vscode editor  |    `"message"` adds action or activity done
|           |                                 |                                                 |   vscode editor  |    [master (root-commit) *hash*] added READEME
|   5       |   `git log`                     |   checks the activities                         |   vscode editor  |    commit *hash* (HEAD -> master) ...

### Create a GitHub Repository
|   Step    |   Code                          |   Action                                           |   Tool/Software  |   Message
|:---------:|---------------------------------|----------------------------------------------------|------------------|-------------------------------
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


|   Link    |     https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
|   Note    |   Follow the instructions provided by GitHub Docs [Steps 2. (Open Git Bash) to 7. (Add the SSH public key to your account on GitHub)]       |


---

### Adding a new SSH key to your GitHub account
<p> Adding SSH key to your GitHub Account, you enable a secure and convenient way to authenticate yourself when interacting with GitHub repositories </p><br>

- Cloning repositories (git clone)
- Pushing Changes (git push)
- Pulling updates (git pull)

|
|   Link:   |   https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account                                                          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Note    |   Follow the instructions provided by GitHub Docs [Steps 1. (Copy the SSH public key to your clipboard.) to 9. (If prompted, confirm access to your account on GitHub.)]       |

---

### Create connection between Repositories (Git Local Repository and GitHub Repositories)
|   Step    |   Code                                                                   |   Action                                        |   Tool/Software  |   Message
|:---------:|--------------------------------------------------------------------------|-------------------------------------------------|------------------|-------------------------------
|   1       |   `git remote add origin git@github.com:<username>/<repository>.git`     |   create a remote connections between two repos |   VSCode         |                                
|   2       |   `git branch -M main`                                                   |   create a main branch                          |   VSCode         |        
|   3       |   `git push -u origin main`                                              |   sends local files to GitHub repository        |   VSCode         |    

|   Notes:                                                                  
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Message prompts: Enumerating objects: n, done. Counting objects ... branch 'main' set up to track 'origin/main'.                                        |
|   Check now your GitHub repository for the file that sends via `git push`                                                                                 |

---

### Create a python script file
|   Step    |   Code                                         |   Action                                     |   Tool/Software  |   Message                             |
|:---------:|------------------------------------------------|----------------------------------------------|------------------|---------------------------------------|
|   1       |   `new-item test.py`                           |   creates a python file                      |   VSCode         |   put script `print("Hello World!")`  |
|           |   `git add test.py`                            |   adds to stagging area                      |   VSCode         |   ready to commit                     |  
|           |   `git commit -m "python file test.py"`        |   creates a python file                      |   VSCode         |   committed, ready for `git push `    |  
|           |   `git push`                                   |   sends file to GitHub repository            |   VSCode         |   check GitHub Repository             |       

---

### Create Python Virtual Environment
|   Step    |   Code                          |   Action                                           |   Tool/Software  |   Message
|:---------:|---------------------------------|----------------------------------------------------|------------------|-----------------------------------------------------------------------
|   1       |   `<git-repository>`            |   go to local repository to your PC                |   Command Prompt |     Navigate the git directory
|   2       |   `python -m venv env`          |   creating virtual environment to local repository |   Command Prompt |     `-m` runs modular, `venv` virtual environment, `env` folder name

|   Notes:                                                                  
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   ... generating virtual environment, check the git repository if the file was create named as `env`. `env` its a typically name for environment.         |

---

### Create .gitignore
|   Step    |   Code                          |   Action                                           |   Tool/Software  |   Message
|:---------:|---------------------------------|----------------------------------------------------|------------------|-----------------------------------------------------------------------
|   1       |   `new-item .gitignore`         |   add message `env/` and save it                   |   VSCode         |     Exclude irrelevant  files to ignore when tracking changes in repo

---

### Activate Python Virtual Environment
|   Step    |   Code                           |   Action                                           |   Tool/Software  |   Message
|:---------:|----------------------------------|----------------------------------------------------|------------------|-----------------------------------------------------------------------
| option 1  |   `env\Scripts\activate.bat`     |   locate folder `env\Scripts\activate.bat`         |   Command Prompt |     Activating virtual enviroment via CMD
| option 2  |   `env\Scripts\Activate.ps1`     |   locate folder `env\Scripts\Activate.ps1`         |   PowerShell     |     Activating virtual enviroment via PowerShell

|   Notes:                                                                  
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   If your see `(env)` at the beginning next in line it means the environment is running.                                                                  |


|   Step    |   Code             |   Action                     |   Tool/Software  |   Message
|:---------:|--------------------|------------------------------|------------------|-----------------------------------------------------------------------
| option 1  |   `deactivate`     |   type the code to deactive  |   Command Prompt |     Activating virtual enviroment via CMD
| option 2  |   `deactivate`     |   type the code to deactive  |   PowerShell     |     Activating virtual enviroment via PowerShell

|   Notes:                                                                  
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Note: Notice if the `(env)` was remove it means the environment is Deactivated                                                                          |

---

### Create requirements.txt for Python Packages
|   Step    |   Code                          |   Action                                           |   Tool/Software  |   Message
|:---------:|---------------------------------|----------------------------------------------------|------------------|-----------------------------------------------------------------------
|   1       |   `new-item requirements.txt`   |   includes package names for Python                |   VSCode         |     Sample packages are: sqlalchemy, pandas, psycop2 and etc.

---

### Download requirements.txt for Python Packages
|   Step    |   Code                          |   Action                                           |   Tool/Software  |   Message
|:---------:|---------------------------------|----------------------------------------------------|------------------|-----------------------------------------------------------------------
|   1       |   `env\Scripts\activate.bat`   |   enable the environment                            |   Command Prompt  |     Sample packages are: sqlalchemy, pandas, psycopg2 and etc.

|   Notes:                                                                  
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Note: If your see `(env)` at the beginning next in line it means the environment is running.                                                            |

|   Step    |   Code                              |   Action                                           |   Tool/Software  |   Message
|:---------:|-------------------------------------|----------------------------------------------------|------------------|-------------------------------------------------------------------
|   2       |   `pip install -r requirements.txt` |  downloads the requirements via `pip` command      | VSCode           | Check `env\Lib\site-packages` where does packages stored
|   3       |   `python`                          |  run python via terminal                           | VSCode           | Check if packages are ready to import
|           |   `import sqlalchemy`               |  importing `sqlalchemy` python package             | VSCode           | 
|           |   `import pandas`                   |  importing `pandas` python package                 | VSCode           | 
|           |   `import psycopg2`                 |  importing `psycopg2` python package               | VSCode           |  

|   Notes:                                                                  
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Any packages that are not included in `requirements.txt` will be unable to import                                                                       |

---

### Add to Stagging Area all modified files
|   Step    |   Code                                          |   Action                        |   Tool/Software  |   Message
|:---------:|-------------------------------------------------|---------------------------------|------------------|-------
|   1       |   `git add .`                                   |   adds to stagging area         |   VSCode         |     Ready to commit
|   2       |   `git commit -m "adds requirements.txt file"`  |   adds commit messages          |   VSCode         |     Ready to push
|   3       |   `git push `                                   |   send files to GitHub Repo     |   VSCode         |     Sends files...

---

| [Botnie Data](https://www.facebook.com/botnie.data/) | <br>
| [Josh Dev](https://www.facebook.com/profile.php?id=100087019650476) | [Josh Dev YouTube Channel](https://www.youtube.com/@joshvaldeleon3138) <br>
| [Data Engineer Pilipinas](https://www.facebook.com/DataEngineeringPilipinas) | [Data Engineer Pilipinas LinkedIn](https://www.linkedin.com/company/dataengineeringpilipinas/) | [Data Engineer Pilipinas GitHub Repo](https://github.com/ogbinar/DataEngineeringPilipinas) 

---

*This README.md file was generated on 20240211 by Botnie Data*
<!-- remove all comments (like this) before final save  -->