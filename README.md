# ${PROJECT}

${DESCRIPTION}

## Initial configuration

1. Configure [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)
1. Install Python packages: `poetry install`
1. Initialize git repository: `git init`
1. Execute `add-author.py` to populate NAME and EMAIL tokens with values from
   Git configuration
1. Install `pre-commit` hooks: `pre-commit install`
