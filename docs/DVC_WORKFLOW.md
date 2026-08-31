# DVC Workflow

## Remote Configuration
DVC remote used:
`myremote` → local DVC remote storage.

## Dataset Versioning Workflow

For every dataset change, the following workflow was used:

1. `dvc add`
2. `git add *.dvc`
3. `git commit`
4. `dvc push`

## Dataset Versions

- Version 1: 150 rows
- Version 2: 170 rows

## Comparing Versions

`git log --oneline -- data/raw/iris_v1.csv.dvc`

`dvc diff 9c87025`

These commands were used to view the dataset history and compare versions.

## Restoring Versions

`git checkout <commit> -- data/raw/iris_v1.csv.dvc`

followed by:

`dvc checkout data/raw/iris_v1.csv.dvc`

was used to restore a historical dataset version.