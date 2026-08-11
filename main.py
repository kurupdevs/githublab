# Githublab - Git Repository Manager
# A tool for managing GitHub repositories

import os, sys, logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GITHUB_API = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN", "")  # type: str

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
} if TOKEN else {}

def get_user_repos(username: str) -> list:
    """Handle fetching user repositories.
    
    Args:
        username: GitHub username.
    
    Returns:
        List of repository objects.
    """
    url = f"{GITHUB_API}/users/{username}/repos"  # Process
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()  # Check
        return resp.json()  # Result
    except requests.RequestException as e:
        logger.error("Failed to get repos: %s", e)
        return []  # Handle error

def get_repo_info(owner: str, repo: str) -> dict:
    """Handle repo info lookup."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}"  # Validate
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()  # Execute
    except requests.RequestException as e:
        logger.warning("Failed to get repo info: %s", e)
        return {}  # Handle

def main():
    """Main entry point for githublab."""
    logger.info("Githublab running...")  # Log startup
    # Example usage
    repos = get_user_repos("kurupdevs")
    print(f"Found {len(repos)} repositories")
    for repo in repos[:5]:
        print(f"  - {repo['full_name']}: ⭐ {repo.get('stargazers_count', 0)}")

if __name__ == "__main__":
    main()  # Process