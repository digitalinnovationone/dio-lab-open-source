## Git's Commands

Welcome to the "Git's Commands" section! This page serves as a comprehensive guide to some of the most fundamental and essential commands in the world of Git. Git is a powerful distributed version control system that enables efficient collaboration, tracking changes, and managing your codebase's history. Whether you're a seasoned developer or just getting started, these commands will be your compass as you navigate through various aspects of version control.
## 🌐 Introduction to Version Control

Version control is like a time machine for your code. It allows you to track changes to your project over time, collaborate seamlessly with teammates, and revert to previous states when needed. Git, as a distributed version control system, empowers developers to work concurrently on the same project, while maintaining a clear record of who made what changes and when.

## ⚙️ Settings Up Git

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
  - Clone only brachys repository
    - `$ git clone -branch [branch_name] [url_remote_origin]`
  - Clone into a specific repository
    - `$ git clone [url_remote_origin] [dir_name]`
  
### Create a new connection with the remote repository
- List remote repositories
  - `$ git remote`
- Create a new connection to remote repository on server
  - `$ git remote add [remote_name] [url_to_remote]`
- Remove a connection to remote repository
  - `$ git remote rm [remote_name]`
- Rename a remote connection
  - `$ git remote rename [remote_old_name] [remote_new_name]`

### Create a new commit
- Include files in stage area
  - `$ git add --all or -a or .` 
- Create a commit with message
  - `$ git commit -m "your message here"`
- Combine all in one commit
  - `$ git commit -a -m "your message here"`
- Change the message to commit
  - `$git commit -amend "new message here"`

### Branching and Merging
- Create a new branch
  - `$ git branch [branch_name]`
- Switch to a branch
  - `$ git checkout [branch_name]`
- Create and switch to a new branch
  - `$ git checkout -b [new_branch_name]`
- List all branches
  - `$ git branch`
- Merge changes from one branch into another
  - `$ git merge [source_branch]`

### Remote Operations
- Fetch changes from a remote repository
  - `$ git fetch [remote_name]`
- Pull changes from a remote repository into the current branch
  - `$ git pull [remote_name] [branch_name]`
- Push local changes to a remote repository
  - `$ git push [remote_name] [branch_name]`
- Push changes and set the upstream branch
  - `$ git push -u [remote_name] [branch_name]`
- Push changes to all remote branches
  - `$ git push --all`

### Viewing Changes
- Show the history of commits
  - `$ git log`
- Show a summarized commit history
  - `$ git log --oneline`
- Show changes between commits
  - `$ git diff [commit_hash]`
- Show changes between the working directory and the last commit
  - `$ git diff`

### Undoing Changes
- Discard changes in the working directory
  - `$ git checkout -- [file]`
- Unstage changes (move changes from staging to working directory)
  - `$ git reset [file]`
- Undo the last commit (keep changes in the working directory)
  - `$ git reset HEAD~1`
- Discard changes in a specific commit
  - `$ git revert [commit_hash]`
- Discard all local changes and pull from remote
  - `$ git fetch origin && git reset --hard origin/master`
  
### Collaboration
- See the list of remote repositories
  - `$ git remote -v`
- Create a pull request (in platforms like GitHub or GitLab)
- Review and merge pull requests


Feel free to incorporate any of these commands and explanations into your README if you think they would be helpful for users looking to learn Git. Remember that the goal is to provide a clear and organized resource for newcomers to understand and use Git effectively.