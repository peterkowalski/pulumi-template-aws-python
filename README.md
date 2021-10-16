# ${PROJECT}

${DESCRIPTION}

## Initial configuration

1. Install [Pulumi](https://www.pulumi.com/docs/get-started/install/)

2. Configure [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

3. Install [Poetry](https://python-poetry.org)

4. Install [pre-commit](https://pre-commit.com/#install)

5. Add `.envrc` file with the following content:

    ```bash
    #! /usr/bin/env bash
    export AWS_PROFILE=$YOUR_AWS_PROFILE
    ```

6. Install Python virtual environment: `poetry install`

7. Install `pre-commit` hooks: `pre-commit install`

8. Login to your AWS backend: `pulumi login $BUCKET`

9. Create Pulumi stack: `pulumi stack init --secrets-provider="$KMS_KEY_ALIAS"`
