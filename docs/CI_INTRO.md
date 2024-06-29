# GitHub Actions: First workflow.
___

## <u> What is GitHub Workflows? </u>
- GitHub Workflows, powered by GitHub Actions, automate software development processes directly from your GitHub repository.
- They allow you to define a series of steps that can be triggered by events like pushes, pull requests, or on a schedule. 
##  <u> Purpose of Workflows? </u>
1. __Continuous Integration (CI)__ : Automatically build, test, and validate your code changes.
2. __Continuous Deployment (CD)__: Deploy your application to various environments after successful tests.
3. __Automation__: Automate routine tasks like merging pull requests, notifying teams, or updating dependencies.
4. __Consistency__: Ensure consistent development practices by automating code quality checks and tests.
### <u> WorkFlow syntax. </u>

- Start By creating yml file in the ```.github/workflows/ci_cd.yml```
 ```bash
 mkdir ".github"
 cd .github && mkdir workflows
 touch workflows/ci.yml
 ```

- In the file (ci_cd.yml), Here is a sample of the code.

```yaml
# The name of the workflow. It can be anything descriptive.
name: CI/CD Pipeline

# on: Defines the events that trigger the workflow.
on:
  # push:: The workflow runs when there is a push event.
  push:
    # branches:: Specifies the branches for the push event.
    branches:
      - main
  # pull_request:: The workflow runs when a pull request 
  # is created or updated
  pull_request:  
    branches:
      - main
# jobs:: A list of jobs to run as part of this workflow.
jobs:
# build:: The identifier for the job, can be named anything 
# descriptive.
  build:
    # runs-on: ubuntu-latest: Specifies the operating system 
    # to run the job on.
    runs-on: ubuntu-latest
    # steps:: A list of steps to execute as part of the job.
    steps:
      # - name: Checkout code: A name for the step, describing 
      # what it does.
      - name: Checkout code 
        # uses: actions/checkout@v2: Uses the checkout action 
        # (Which is a community open source repository)
        # to pull the repository code into the runner.
        uses: actions/checkout@v2
        
      - name: Set up Python
        uses: actions/setup-python@v2
        # with:: Additional parameters for the setup-python action.
        with:
          # python-version: '3.8': Specifies the version of Python 
          # to set up.
          python-version: '3.10'

      - name: Install dependencies
        # run: |: Indicates that the following lines are commands to run.
        run: |  
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest

```
### <u> Effective Ways to Use GitHub Workflows. </u>

1. Automated Testing:
    - Unit Tests: Run unit tests on every push or pull request to ensure code changes do not break functionality.
    - Integration Tests: Perform integration tests to validate interactions between different parts of the application.

2. Continuous Deployment:
    - Deploy applications to staging or production environments after successful tests.
    - Use workflows to automate the deployment process, reducing manual intervention and errors.

3. Code Quality and Security:
    - Integrate tools like linters, formatters, and security scanners to maintain code quality and detect vulnerabilities.
    - Run these tools on pull requests to catch issues early in the development process.

4. Automated Releases:
    - Use workflows to create releases, generate changelogs, and publish release notes automatically.
    - Tag and version your codebase using workflows for consistent release management.

5. Environment Management:
    - Define different workflows for different environments (development, staging, production) to manage deployments and tests effectively.
    - Use environment-specific secrets and configurations securely.

6. Notifications and Alerts:
    - Integrate with communication tools like Slack or Microsoft Teams to send notifications on workflow status.
    - Notify teams about build failures, deployment status, or critical issues.

7. Documentation and Training:
    - Use workflows to generate and publish documentation automatically.
    - Automate the setup of development environments for new team members, ensuring consistency.

### <u> Basic CI Workflow for a Python Project. </u>

```yaml
name: Django CI
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest

```
### <u> Best Practices.  </u>
1. __Modular Workflows:__ Break down workflows into smaller, reusable components to make them easier to manage and maintain.
2. __Secrets Management:__ Use GitHub Secrets to store sensitive information securely and access them in workflows.
3. __Caching:__ Utilize caching strategies to speed up workflow runs, especially for dependencies.
4. __Parallelism:__ Run jobs in parallel where possible to reduce overall workflow execution time.
5. __Fail Fast:__ Configure workflows to fail early if a critical step fails, saving time and resources.
6. __Documentation:__ Document your workflows to help team members understand the automation processes and contribute effectively.




