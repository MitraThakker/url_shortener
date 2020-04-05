from aws_cdk import core, aws_dynamodb, aws_lambda


class UrlShortenerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dynamodb_table = aws_dynamodb.Table(self, 'mapping-table',
                                            partition_key=aws_dynamodb.Attribute(
                                                name='id',
                                                type=aws_dynamodb.AttributeType.STRING
                                            ))

        lambda_function = aws_lambda.Function(self, 'backend',
                                              runtime=aws_lambda.Runtime.PYTHON_3_7,
                                              handler='handler.main',
                                              code=aws_lambda.Code.asset('./lambdas'))
