# Git commands.
___
### <u>Creating new branch.</u>
```bash
git branch <branch_name>
# or
git checkout -b <branch name>
# Confirm the branch you're in
git branch
# Create branch from another branch.
git checkout -b <new_branch> <from_branch>
```
### <u>Merging two branches.</u>
```bash
# Use git checkout to switch to the branch you 
# want to merge into. i.e merge to main
git checkout main
# Next, use git merge and specify the name of 
# the other branch to bring into this branch
git merge production # (fast-forward merge)
# Work continues on the main and other 
# branches, so they no longer share a common
# commit history. Now a developer wants to merge the 
# featureX branch into the main branch.
git merge featureX # (three-way (or recursive) merge)
```
### <u>Merging Branches to Remote Repository.</u>
If you create a branch in your local repository,the 
remote repository is not aware of the branch’s existence. 
Before you can push the branch code in the remote repository, 
you set the remote repository as the upstream branch using 
the ``git push`` command.
```bash
git push --set-upstream origin <the_new_branch>
# Probably the main branch is already merged with other branches
# Use
git merge main
```
### <u>Pull requests.</u>
Pull requests let you tell others about changes you've 
pushed to a branch in a repository on GitHub. 
Once a pull request is opened, you can discuss and review the 
potential changes with collaborators and add follow-up commits 
before your changes are merged into the base branch.


