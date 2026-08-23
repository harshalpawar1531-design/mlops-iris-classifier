# Version Control Workflow

## Project
MLOps Iris Classifier

## Branches
- main
- develop
- feature/add-classification-report
- conflict-demo-a
- conflict-demo-b

## Git Workflow
1. Created the project and initialized Git.
2. Created and pushed the main branch to GitHub.
3. Created the develop branch.
4. Created feature/add-classification-report branch.
5. Updated the training script and committed the changes.
6. Pushed the feature branch to GitHub.
7. Created a Pull Request from feature/add-classification-report to develop.
8. Merged the Pull Request.
9. Created conflict-demo-a and conflict-demo-b.
10. Modified README.md differently in both branches.
11. Created a merge conflict in README.md.
12. Resolved the conflict and created a merge commit.
13. Tested the project using:
   python src/train.py

## Verification
- Git repository contains 3+ branches.
- A Pull Request was successfully merged.
- Merge conflict was successfully created and resolved.
- Training script runs successfully.
- Classification report and Accuracy are displayed.
- Model is saved to models/iris_model.joblib.