# ${PROJECT} BUGFIX

${DESCRIPTION}

## Initial configuration

1. Create new project directory and go to it

1. Execute `pulumi new https://github.com/peterkowalski/pulumi-template-aws-python`

1. Open workspace in Visual Studio Code using Dev Container

1. Configure [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

1. Remove `venv` directory

1. Remove virtual environment configuration from `Pulumi.yaml`

    BEFORE:

    ```yaml
    name: ${PROJECT}
    runtime:
    name: python
    options:
        virtualenv: venv
    main: src/
    description: ${DESCRIPTION}
    ```

    AFTER:

    ```yaml
    name: ${PROJECT}
    runtime:
      name: python
    main: src/
    description: ${DESCRIPTION}
    ```

1. Install Python packages: `poetry install`

1. Initialize git repository: `git init`

1. Execute `fix_template.py`

1. Install `pre-commit` hooks: `pre-commit install`

1. Make an initial commit

## Roadmap

* Automatically remove initially created `venv` directory with `fix_template.py`
* Automatically remove virtual environment configuration from
  `Pulumi.yaml` with `fix_template.py`
