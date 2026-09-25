# Version Control Workflow for ML Projects

## 1. Introduction

Version control is essential for Machine Learning projects because it helps track code changes, collaborate with team members, and maintain different versions of the project.

Git is used for version control, while GitHub is used for remote repository hosting and collaboration.

## 2. Branching Strategy

The project uses the following branches:

- `main` – Stable production-ready code.
- `develop` – Integration branch for development.
- `feature/*` – Used for developing individual features.
- `conflict-demo-*` – Used for demonstrating merge conflicts.

## 3. Basic Git Workflow

The basic workflow is:

1. Create or clone the repository.
2. Create a feature branch.
3. Make changes to the project.
4. Check the changes using `git status`.
5. Stage changes using `git add`.
6. Commit changes using `git commit`.
7. Push the branch to GitHub.
8. Create a Pull Request.
9. Review and merge the Pull Request.
10. Update the local `develop` branch.

## 4. Merge Conflict Resolution

Merge conflicts can occur when two branches modify the same file.

The conflict is resolved by:

1. Identify the conflicted file using `git status`.
2. Open the file in VS Code.
3. Review the conflicting changes.
4. Select the required change.
5. Save the file.
6. Run `git add`.
7. Commit the merge using `git commit`.

## 5. ML Project Best Practices

- Use meaningful commit messages.
- Keep commits small and focused.
- Use branches for individual features.
- Keep `main` stable.
- Use Pull Requests for collaboration.
- Use `.gitignore` to avoid committing unnecessary files.
- Use DVC for large datasets and ML model files.

## 6. Conclusion

A structured Git workflow helps ML teams track changes, collaborate effectively, resolve conflicts, and maintain a clean project history.