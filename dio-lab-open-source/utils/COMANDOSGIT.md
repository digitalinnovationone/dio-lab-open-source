# Git's Commands

This page is about some commands from Git. 

😁 You also can contribute!

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