brew install amazon-ecs-cli

aws cloudformation create-stack --stack-name TextClassificationECSCluster --template-body file://ecs-text-classification-web-service.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation wait stack-create-complete --stack-name TextClassificationECSCluster