import json
import os

import jinja2
from github import Github, GithubException


def create_readme_file():
    """Creates the contents of a README.md file from a jinja2 template"""
    template_loader = jinja2.FileSystemLoader("./templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("README.j2")
    return template.render()


def create_issue_body(default_branch_name):
    """Creates the body contents of a GitHub issue from a jinja2 template"""
    template_loader = jinja2.FileSystemLoader("./templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("issue.j2")

    template_args = {
        'default_branch_name': default_branch_name,
        'branch_protections': ['Require code owner review', 'Require approving review count', 'Enforce admins']
    }

    return template.render(template_args)


def lambda_handler(event, context):
    access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
    payload_body = event.get('body', {})
    body = json.loads(payload_body)
    event_action = body['action']

    # Act only on repository "created" actions, ignore the rest
    if event_action == 'created':
        repo_name = body['repository']['full_name']

        github = Github(access_token)
        repository = github.get_repo(repo_name)
        default_branch_name = repository.default_branch

        try:
            default_branch = repository.get_branch(default_branch_name)
        except GithubException as ex:
            # If no branch has been created, create a README.md file and push it to the repository
            readme_content = create_readme_file()
            repository.create_file("README.md", content=readme_content, message="Automatic creation of README.md file",
                                   branch=default_branch_name)
            default_branch = repository.get_branch(default_branch_name)

        if not default_branch.protected:
            default_branch.edit_protection(
                require_code_owner_reviews=True,
                required_approving_review_count=1,
                enforce_admins=True
            )
            repository.create_issue(
                title=f":robot: Automatic branch protection - {default_branch_name}",
                body=create_issue_body(default_branch_name),
                labels=["automation", "security checks"]
            )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Branch protections enabled",
            }),
        }
    else:
        return {
            "statusCode": 204,
            "body": json.dumps({
                "message": "Nothing to do"
            })
        }
