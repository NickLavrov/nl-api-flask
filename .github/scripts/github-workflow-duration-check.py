import datetime
import os
import requests

# Constants
GITHUB_API = 'https://api.github.com'
REPO_OWNER = 'NickLavrov'
REPO_NAME = 'nl-api-flask'
WORKFLOW_FILE = 'push-image-and-deploy-preprod.yml'
JOB_NAME = 'push-image'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
EXCLUDED_BRANCHES = os.getenv('EXCLUDED_BRANCHES', '').split(',')
NUM_RUNS = 50  # Number of runs to consider

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_workflow_runs():
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/runs"
    params = {
        'status': 'success',
        'per_page': NUM_RUNS
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json().get('workflow_runs', [])

def get_job_duration(run_id):
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}/jobs"
    response = requests.get(url, headers=headers)
    jobs = response.json()['jobs']
    for job in jobs:
        if job['name'] == JOB_NAME:
            start_time = datetime.datetime.fromisoformat(job['started_at'].rstrip('Z'))
            end_time = datetime.datetime.fromisoformat(job['completed_at'].rstrip('Z'))
            duration = end_time - start_time
            return duration.total_seconds()
    return None

def main():
    runs = get_workflow_runs()
    durations = []
    for run in runs:
        if run['head_branch'] not in EXCLUDED_BRANCHES:
            duration = get_job_duration(run['id'])
            if duration:
                durations.append(duration)
                print(f"Run URL: {run['html_url']}, Duration: {duration} seconds")

    if durations:
        average_duration = sum(durations) / len(durations)
        print(f"Average Duration: {average_duration} seconds")
        print(f"Min Duration: {min(durations)} seconds")
        print(f"Max Duration: {max(durations)} seconds")
    else:
        print("No runs found for the specified criteria.")

if __name__ == "__main__":
    main()
