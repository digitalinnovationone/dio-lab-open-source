# Git's Commands

This page is about some commands from Git. 

😁 You also can contribute!

## ⚙️ Settings Up Git
- Check your current e-mail and username configuration:
  - `$ git config user.email`
  - `$ git config user.name`
- Configure your email 
  -  `$ git config user.email [your_mail_here]`
- Configure your user name 
  - `$ git config user.name [your_user_here]`
  
If you want to config your scope of work use the tags below.

- Local scope 
  - `$ git config --local user.email [your_mail_here]`
- Global scope 
  - `$ git config --global user.email [your_mail_here]`
- System scope 
  - `$ git config --system user.email [your_mail_here]`

## 📚 Basics Commands

### Create a new repository
  - Create a local repository
    - `$ git init`
  - Clone a remote repository
    - `$ git clone [url_remote_origin]`
  - Clone a specific branch of a repository
    - `$ git clone -b [branch_name] [url_remote_origin]`
  - Clone into a specific repository
    - `$ git clone [url_remote_origin] [dir_name]`
  
  
### Create a new connection with the remote repository
- List remote repositories
  - `$ git remote`
- View details of a specifc remote repository
  - `$ git remote show [remote_name]`
- Fetch the latest changes from a remote repository (without merging)
  - `$ git fetch [remote_name]`
- Create a new connection to remote repository on server
  - `$ git remote add [remote_name] [url_to_remote]`
- Remove a connection to remote repository
  - `$ git remote rm [remote_name]`
- Rename a remote connection
  - `$ git remote rename [remote_old_name] [remote_new_name]`

### Create a new commit
- View the status of your changes
  - `$ git status`
- View the log of commits
  - `$ git log`
- View a brief log of commits with graphical representation
  - `$ git log --oneline --graph`
- Include specific files in the staging area
  - `$ git add [file1] [file2] ...`
- Remove files from the staging area
  - `$ git reset [file1] [file2] ...`
- Include files in stage area
  - `$ git add --all or -a or .` 
- Create a commit with message
  - `$ git commit -m "your message here"`
- Combine all in one commit
  - `$ git commit -a -m "your message here"`
- Change the message to commit
  - `$git commit -amend "new message here"`
- Change the message of the last commit
  - `$ git commit --amend -m "new message here"`

### Branching and Merging
- List all branches:
  - `$ git branch`
- Create a new branch:
  - `$ git branch [branch_name]`
- Switch to a different branch:
  - `$ git checkout [branch_name]`
- Create and switch to a new branch in one command:
  - `$ git checkout -b [branch_name]`
- Merge changes from one branch into another:
  - `$ git merge [source_branch]`
- Delete a branch:
  - `$ git branch -d [branch_name]`