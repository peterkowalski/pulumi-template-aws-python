"""An AWS Python Pulumi program."""

import pulumi_aws as aws
import pulumi

from common import register_auto_tags
import configuration

config = configuration.load()
register_auto_tags({
    "Project": config["metadata"]["project"],
    "Stack": config["metadata"]["stack"],
    "Owner": config["tagging"]["owner"],
    "Environment": config["tagging"]["environment"],
})

resource_name_prefix = f'{config["metadata"]["project"]}-{config["metadata"]["stack"]}'

# Create an AWS resource (S3 Bucket)
bucket = aws.s3.Bucket(f'{resource_name_prefix}-my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
