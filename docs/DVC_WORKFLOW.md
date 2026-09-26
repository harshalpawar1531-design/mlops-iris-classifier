# DVC Workflow for Dataset Versioning

## 1. DVC Remote Configuration

A local folder was configured as the DVC remote:

`~/dvc-remote-storage`

The remote was configured using:

`dvc remote add -d myremote ~/dvc-remote-storage`

## 2. Dataset Versioning Workflow

For each dataset change, the following workflow was used:

1. Modify the dataset.
2. Run `dvc add`.
3. Run `git add` on the `.dvc` metafile.
4. Commit the `.dvc` file using Git.
5. Run `dvc push` to upload the data to the DVC remote.

## 3. Dataset Versions

### Version 1

- Dataset: `iris_v1.csv`
- Rows: 150
- Git commit: `5e16b46`

### Version 2

- Dataset: `iris_v1.csv`
- Rows: 170
- Git commit: `1ecebca`
- 20 synthetic rows were added.

## 4. Comparing Dataset Versions

`dvc diff 5e16b46`

was used to compare the current dataset with Version 1.

The result showed:

`data/raw/iris_v1.csv` as modified.

## 5. Restoring Dataset Versions

To restore Version 1:

`git checkout 5e16b46 -- data/raw/iris_v1.csv.dvc`

followed by:

`dvc checkout data/raw/iris_v1.csv.dvc`

The latest Version 2 was restored using:

`git checkout HEAD -- data/raw/iris_v1.csv.dvc`

followed by:

`dvc checkout data/raw/iris_v1.csv.dvc`

## 6. Conclusion

DVC was successfully integrated with Git to version the Iris dataset. Two dataset versions were created and compared, and historical data versions were restored using DVC checkout.