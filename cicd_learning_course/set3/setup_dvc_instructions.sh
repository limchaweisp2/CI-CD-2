#!/bin/bash
# Run these commands locally to setup DVC as described in the PDF

# Source: PDF 4, Page 17 (Install)
pip install dvc

# Source: PDF 4, Page 18 (Init)
dvc init

# Source: PDF 4, Page 26 (Local and Default Remotes)
# Using /tmp/dvc to simulate a remote storage without cloud creds
dvc remote add -d mylocalremote /tmp/dvc

# Source: PDF 4, Page 19 (Adding Files to DVC)
dvc add weather.csv
git add weather.csv.dvc .gitignore
git commit -m "Initialize DVC"
