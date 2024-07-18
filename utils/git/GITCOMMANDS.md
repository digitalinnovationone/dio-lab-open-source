[![Read in Portuguese](https://img.shields.io/badge/%F0%9F%87%A7%F0%9F%87%B7%20Portugu%C3%AAs-gray.svg)](COMANDOSGIT.md)
[![Read in English](https://img.shields.io/badge/%F0%9F%87%BA%F0%9F%87%B8%20English-F0FFFF.svg)](GITCOMMANDS.md)

# Git Commands

This document provides an overview of essential Git commands.

😁 Feel free to contribute and enhance this guide!

## Table of Contents
- [⚙️ Setting Up Git](#setting-up-git)
- [📚 Basic Commands](#basic-commands)
    - [Repository Operations](#repository-operations)
    - [Remote Connections](#remote-connections)
    - [Commit Operations](#commit-operations)
- [📈 Intermediate Git Commands](#intermediate-git-commands)
    - [Branching and Merging](#branching-and-merging)
    - [Stashing Changes](#stashing-changes)
    - [Rewriting History](#rewriting-history)
    - [Remote Repositories](#remote-repositories)
    - [Inspecting Changes](#inspecting-changes)
- [🧠 Advanced Git Commands](#advanced-git-commands)
    - [Refs and the Reflog](#refs-and-the-reflog)
    - [Bisecting](#bisecting)
    - [Filter-branch](#filter-branch)
    - [Submodules](#submodules)
    - [Worktrees](#worktrees)
    - [Advanced Rebase](#advanced-rebase)
    - [Cleanup](#cleanup)
    - [Cherry-picking](#cherry-picking)
    - [Advanced Merge](#advanced-merge)

️️
<a id="setting-up-git"></a>
## ⚙️ Setting Up Git

- **Configuring your email**:
  ```bash
  $ git config user.email [your_mail_here]
  ```

- **Configuring your username**:
  ```bash
  $ git config user.name [your_user_here]
  ```

If you need to specify the scope for your configuration, use the tags below:

- **Local scope** (specific to the current repository):
  ```bash
  $ git config --local user.email [your_mail_here]
  ```

- **Global scope** (applies to all repositories on your system):
  ```bash
  $ git config --global user.email [your_mail_here]
  ```

- **System scope** (applies system-wide, affecting all users):
  ```bash
  $ git config --system user.email [your_mail_here]
  ```
<a id="basic-commands"></a>
## 📚 Basic Commands

### Repository Operations

- **Initializing a new local repository**:
  ```bash
  $ git init
  ```

- **Cloning an existing remote repository**:
  ```bash
  $ git clone [url_remote_origin]
  ```

- **Cloning a specific branch**:
  ```bash
  $ git clone --branch [branch_name] [url_remote_origin]
  ```

- **Cloning into a specified directory**:
  ```bash
  $ git clone [url_remote_origin] [dir_name]
  ```

### Remote Connections

- **Listing connected remote repositories**:
  ```bash
  $ git remote
  ```

- **Adding a new remote connection**:
  ```bash
  $ git remote add [remote_name] [url_to_remote]
  ```

- **Removing an existing remote connection**:
  ```bash
  $ git remote rm [remote_name]
  ```

- **Renaming a remote connection**:
  ```bash
  $ git remote rename [remote_old_name] [remote_new_name]
  ```

### Commit Operations

- **Staging all changes for commit**:
  ```bash
  $ git add --all
  ```
  or
  ```bash
  $ git add -a
  ```
  or simply
  ```bash
  $ git add .
  ```

- **Committing staged changes with a message**:
  ```bash
  $ git commit -m "your message here"
  ```

- **Staging and committing all changes in one step**:
  ```bash
  $ git commit -a -m "your message here"
  ```

- **Modifying the most recent commit message**:
  ```bash
  $ git commit --amend -m "new message here"
  ```

<a id="intermediate-git-commands"></a>
## 📈 Intermediate Git Commands

### Branching and Merging

- **Listing all local branches in the current repository**:
  ```bash
  $ git branch
  ```

- **Switching to a branch**:
  ```bash
  $ git checkout [branch_name]
  ```

- **Creating and switching to a new branch**:
  ```bash
  $ git checkout -b [branch_name]
  ```

- **Merging a branch into the active branch**:
  ```bash
  $ git merge [branch_name]
  ```

- **Deleting a branch**:
  ```bash
  $ git branch -d [branch_name]
  ```

### Stashing Changes

- **Stashing current changes**:
  ```bash
  $ git stash
  ```
  Temporarily saves changes that are not yet committed.

####
####

- **Stashing current changes with a message**:
  ```bash
  $ git stash save "Your message here"
  ```
  Temporarily saves changes that are not yet committed with a descriptive message.

####
####

- **Listing all stashed changes**:
  ```bash
  $ git stash list
  ```
  Shows a list of all the stashed changes.

####
####

- **Applying a specific stash**:
  ```bash
  $ git stash apply stash@{n}
  ```
  Restores the stashed changes from a specific stash, where `n` is the stash number (e.g., `stash@{0}`, `stash@{1}`).

####
####

- **Applying most recent stash**:
  ```bash
  $ git stash apply
  ```

- **Dropping a stash**:
  ```bash
  $ git stash drop
  ```
  Removes the latest stash.

####
####

- **Dropping a specific stash**:
  ```bash
  $ git stash drop stash@{n}
  ```
  Removes a specific stash based on the number `n`.

####
####

- **Applying and dropping the latest stash**:
  ```bash
  $ git stash pop
  ```
  Applies the latest stash and then removes it from the stash list.

####
####

### Rewriting History

- **Rebasing your branch**:
  ```bash
  $ git rebase [base_branch]
  ```
Reapplies your branch's commits onto the base branch. Useful for ensuring a linear history.

####
####

- **Interactive rebasing**:
  ```bash
  $ git rebase -i [base_commit]
  ```
  Allows you to edit commits in the process.

####
####

- **Continue rebasing after resolving conflicts**:
  ```bash
  $ git rebase --continue
  ```

####
####

- **Abort the current rebase**:
  ```bash
  $ git rebase --abort
  ```

####
####

- **Amending the latest commit (without changing commit message)
  ```bash
  $ git commit --amend --no-edit
  ```
  Allows you to add new changes to the previous commit without changing its commit message.

####
####

### Remote Repositories

- **Fetching changes from remote without merging**:
  ```bash
  $ git fetch [remote_name]
  ```
  This command retrieves updates from a remote repository but doesn't merge these changes with your local branch. It's useful to see updates before deciding whether you want to integrate them.

####
####

- **Pulling changes from a remote repository**:
  ```bash
  $ git pull [remote_name] [branch_name]
  ```
  This command fetches and automatically tries to merge changes from the specified remote branch with your current local branch.

####
####

- **Pushing a branch to remote**:
  ```bash
  $ git push [remote_name] [branch_name]
  ```
  Pushes your local changes to the remote repository. This updates the remote branch with your recent commits.

####
####

- **Configurando uma conexão de rastreamento entre um branch local e um branch remoto / Setting up a tracking connection between a local and remote branch**:
  ```bash
  $ git branch --u [remote_name]/[branch_name]
  ```
  Establishes a tracking connection between the local branch and the specified remote branch. This is handy as it allows `git pull` and `git push` to automatically know which remote branch to pull from or push to.

####
####

- **Pulling changes and rebasing (instead of merging)**:
  ```bash
  $ git pull --rebase
  ```
  Instead of merging commits, this command reapplies your local commits on top of the fetched changes. It helps to maintain a clean, linear commit history.

####
####

### Inspecting Changes

- **View commit history**:
  ```bash
  $ git log
  ```

- **Viewing the diff for the staged changes**:
  ```bash
  $ git diff --staged
  ```
  Displays the difference between the staged changes and the latest commit.

- **View difference between the current branch and another branch**:
  ```bash
  $ git diff [other_branch_name]
  ```

- **Viewing the log in a graphical interface**:
  ```bash
  $ gitk
  ```
  Opens a graphical interface to navigate and inspect the commit history (Availability of `gitk` may vary based on installation and OS).

####

- **Logging in a pretty format with one line per commit**:
  ```bash
  $ git log --oneline --graph --all --decorate
  ```
  Displays the commit history in a concise format with branches and tags, making it easier to understand the repository's history.

<a id="advanced-git-commands"></a>
## 🧠 Advanced Git Commands

### Refs and the Reflog

- **Viewing the reflog**:
  ```bash
  $ git reflog
  ```
  Shows a log of where your HEAD and branch references have been. This can be used to recover lost commits or branches.

- **Reapply a lost commit:**:
  ```bash
  $ git cherry-pick [commit_hash]
  ```
  This can be used after consulting the reflog to apply a commit that was lost (due to reset, rebase, etc.)

- **Recover a state after a hard reset**:
  ```bash
  $ git reset 'HEAD@{1}'
  ```
This command lets you go back to the previous state before the hard reset.

### Bisecting

- **Start the bisect process**:
  ```bash
  $ git bisect start
  ```

- **Mark a commit as good**:
  ```bash
  $ git bisect good
  ```

- **Mark a commit as bad**:
  ```bash
  $ git bisect bad
  ```

- **End the bisect process**:
  ```bash
  $ git bisect reset
  ```

- **Using bisect to find a bad commit**:
  ```bash
  $ git bisect start
  $ git bisect bad
  $ git bisect good [last_known_good_commit_hash]
  ```
  Git will then check out a commit halfway between the last known good commit and the end of your branch. Test the commit, then tell Git whether it's good or bad. Git will continue narrowing down until it identifies the exact commit that introduced an issue.

### Filter-branch

- **Replacing all email addresses in history**:
  ```bash
  $ git filter-branch --commit-filter 'if [ "$GIT_AUTHOR_EMAIL" = "old_email@example.com" ]; then
       export GIT_AUTHOR_EMAIL=new_email@example.com;
       export GIT_COMMITTER_EMAIL=new_email@example.com;
     fi;
     git commit-tree "$@"'
  ```
  ⚠️ **Warning**: This command rewrites the history to completely replace email addresses throughout the repository. Proceed with extreme caution!

####
####

- **Removing a file from the entire Git history**:
  ```bash
  $ git filter-branch --force --index-filter "git rm --cached --ignore-unmatch path_to_file" --prune-empty --tag-name-filter cat -- --all
  ```
  ⚠️ **Warning**: This command rewrites the history to completely remove a file from the repository. Proceed with extreme caution!

####
####

### Submodules

- **Adding a submodule**:
  ```bash
  $ git submodule add [repository_url] [path_to_place_submodule]
  ```
  Adds another repository as a submodule in your current repo. This allows you to include and track another project within your own project.

####
####

- **Updating all submodules**:
  ```bash
  $ git submodule update --recursive --remote
  ```

### Worktrees

- **Creating a new worktree**:
  ```bash
  $ git worktree add [path] [branch]
  ```
  This allows you to check out multiple branches simultaneously in different directories.

####
####

### Advanced Rebase

- **Starting an Interactive Rebase**:
  ```bash
  $ git rebase -i [base_branch_name]
  ```

- **Squashing the last *n* commits into a single one**:
  ```bash
  $ git rebase -i HEAD~[n]
  ```
  In the text editor that pops up, replace "pick" with "squash" or "s" for the commits you want to squash into the previous one (the one above them).

####
####

### Cleanup

- **Cleaning untracked files**:
  ```bash
  $ git clean -f
  ```
  ⚠️ **Warning**: Permanently deletes untracked files from the working directory. Always double-check before executing.

####

- **Cleaning Untracked Files and Directories**:
  ```bash
  $ git clean -f -d
  ```
  ⚠️ **Warning**: Permanently removes untracked files and directories. Check carefully before executing.

####

- **Removing remote branches that no longer exist**:
  ```bash
  $ git fetch -p
  ```

- **Cleaning up local branches that have been merged**:
  ```bash
  $ git branch --merged | xargs git branch -d
  ```
  ⚠️ **Warning**: Ensure you no longer need the branches before removing them.

####

### Cherry-picking

- **Applying changes from specific commits**:
  ```bash
  $ git cherry-pick [commit_hash1] [commit_hash2]
  ```

- **Aborting cherry-pick**:
  ```bash
  $ git cherry-pick --abort
  ```
  ⚠️ **Warning**: Aborting the operation will revert any changes applied during the cherry-pick.

####


### Advanced Merge

- **Merging without an automatic commit**:
  ```bash
  $ git merge [branch_name] --no-commit
  ```

- **Merging and squashing all commits**:
  ```bash
  $ git merge --squash [branch_name]
  ```

  This takes all the commits from another branch and squashes them into a single commit on the current branch.

####

- **Previewing merge conflicts before merging**:
  ```bash
  $ git diff --name-only --diff-filter=U
  ```

- **Aborting a merge operation**:
  ```bash
  $ git merge --abort
  ```
  ⚠️ **Warning**: Aborting the merge will revert any changes made during the merge operation.

###

#### 😄 We hope that this guide has been helpful for you. If you have any feedback or would like to contribute with more information, please make a pull request or open an issue!