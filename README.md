# GitHub Repository Manager

This project demonstrates how to automatically enable branch protection in every new repository created in a [GitHub Organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations).

This is accomplished by using organization [webhooks](https://docs.github.com/en/rest/reference/orgs#webhooks) to send an HTTP POST payload to a third-party service that uses the GitHub [REST API](https://docs.github.com/en/rest) to programmatically enable protection on the default branch of the newly created repository.

The third-party service is implemented in python as a serverless [AWS Lambda](https://aws.amazon.com/lambda/) function.

:bulb: The third-party service can be implemented in any programming language and deployed to any platform as long it is able to receive events sent by the Organization webhook. You can even use [ngrok](https://ngrok.com/) or similar solutions to expose the service directly from an http server running in localhost.

GitHub provides the [Octokit library](https://docs.github.com/en/rest/overview/libraries) in Ruby, .Net and Javascript. [Third-party libraries](https://docs.github.com/en/rest/overview/libraries#third-party-libraries) are also available to support other languages.

This project uses the [PyGitHub](https://github.com/PyGithub/PyGithub) library to manage GitHub resources.

## Getting Started

These instructions will guide you on building and deploying the AWS Lambda function and configuring the GitHub organization webhook.

### Prerequisites
- [GitHub](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account) personal account
- [AWS Free Tier](https://aws.amazon.com/free/) account
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Python 3](https://www.python.org/downloads/)
- [Docker](https://hub.docker.com/search/?type=edition&offering=community) - For testing the AWS Lambda function locally

### GitHub Personal Access Token
To enable communication between the serverless function and the GitHub API you will need to generate a GitHub personal access token.

Please follow the [documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create one.

For this example, only the **public_repo** scope is needed.

![Personal Access Token Scopes](images/pat_scopes.png)

:warning: Save the personal access token in a safe place, it will be used later in this guide.

See GitHub's documentation to learn more about [scopes](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).
### AWS Lambda

#### Setup
- [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) and login to your account
- Clone this repository and switch to the location where the repository was cloned

	```bash
	git clone https://github.com/org-acme/repo-manager.git
	```
- Open the file named [template.yaml](template.yaml) in an editor and fill the environment variable named `GITHUB_ACCESS_TOKEN` with the token generated previously
	
	:warning: Don't commit and push this file to your repository!
	
	![Fill personal access token in cloud formation template](images/pat_template.png)
	
	This file is a [AWS CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html) used to create resources in AWS.

- Save the changes to the template file

### Building the project


### GitHub

### Testing

Add additional notes about how to deploy this on a live system



## Contributing

Please feel free to raise issues or submit pull requests to improve this project.

## Authors

* **Jose Mayorga** - *Initial work*

See also the list of [contributors](https://github.com/org-acme/repo-manager/contributors) who participated in this project.

## License

See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [README](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) Template
* [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html)
*
