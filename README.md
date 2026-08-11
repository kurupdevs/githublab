# Githublab

A simple GitHub repository management tool.

## Features

- List user repositories
- Get repository information
- Star count checker

## Setup

```bash
pip install -r requirements.txt
export GITHUB_TOKEN="your_token"
python main.py
```

## Usage

```python
from main import get_user_repos, get_repo_info

# Get repos
repos = get_user_repos("username")

# Get info
info = get_repo_info("owner", "repo")
```

Built by [kurupdevs](https://github.com/kurupdevs)
