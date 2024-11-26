import os
import requests
import subprocess
from loguru import logger

organization = "platanus-hack"
token = ""

url = f"https://api.github.com/orgs/{organization}/repos"

headers = {}
if token:
    headers["Authorization"] = f"token {token}"

response = requests.get(url, headers=headers)
if response.status_code != 200:
    logger.error(f"There was an error: {response.status_code}")
    exit()

repos = response.json()

output_dir = "../data/raw"
os.makedirs(output_dir, exist_ok=True)

for repo in repos:
    repo_name = repo["name"]
    clone_url = repo["clone_url"]
    logger.info(f"Cloning {repo_name}...")
    subprocess.run(["git", "clone", clone_url, os.path.join(output_dir, repo_name)])

logger.info("Done!")
