# AB Project One by Alexandre Borsato - Sept/2024

I am starting learning git/github.

## 📚 This file aims to provide some guidance around git and github / and, git/github steps / commands

You can create readme files thru the [readme editor tool](https://readme.so/pt/editor) 

You can add emojis with the Command Control Space sequence 👍🏻

[GitHub Documents](https://docs.github.com/en)  

[Git Documents](https://git-scm.com/doc)

[Class Documents](https://github.com/elidianaandrade/dio-curso-git-github?tab=readme-ov-file)

## 👨🏽‍💻 Classes Summary

|    Class  |   Summary |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

````
git init
````
````
git clone
````

$ git status = shows the current status in the current directory (repository);

$ cat config = shows the current configuration of the current repo;

$ touch filename = create a file with the name = filename;

$ git add filename = add the file into the staging area to clone/commit
$ git add . = when using with a dot it will add all files in that directory to the staging area to be committed. 

$ git commit -m"first commit" = commit the filename into the github  / -m is used to comment the commitment

$ git log = shows the executions
$ git reflog = shows the committ executions including the ones done with "git reset"

$ git restore filename = restore the file status before last commit  ((( R E V I E W )))
$ git reset (--soft or --mixed or --hard) = rollback the last commit before changes  soft: returns to staging area / mixed: returns to pre-staging area and requires a new git add command  / hard: cancell entirelly  ((( R E V I E W )))

-- git restore and git reset should be done before any git clone, so, you will just clone and share with others the right version you want
--------------------------------------------------------------------------------------------------------------------------------------------

### to push / clone the files into the github remote repo:

$ git remote add origin https://github.com/alexandreborsato/ab01.git  =  remote - indicates that we are commanding remote github / add into the origin and the https address to manage the remote repo (you can get it viewing inside github repo (cod))

$ git push -u origin main = do the files push to the main branch

### to pull the changes from the remote github to the local repo you can use the $ git pull
$ git pull

### git fetch
$ git fetch origin main =  it pulls the last commits from the remote github to local repo without merging with local files so you can review both
$ git diff main origin/main = it shows the differences between local and remote
$ git merge origin/main = after you decide to merge it will merges the content from remote with local

### working with branchs
    git checkout - creates new branch
    git branch - list the branchs  ( -d  deletes the branch - example: git branch -d test  :: it deletes the branch named test)
    git merge - merge branchs

