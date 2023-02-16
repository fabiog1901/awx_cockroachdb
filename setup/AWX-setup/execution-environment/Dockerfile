FROM quay.io/ansible/awx-ee:latest

USER root

RUN pip install --upgrade pip

RUN ansible-galaxy collection install ansible.posix

RUN ansible-galaxy collection install community.general

RUN pip install boto boto3 botocore 

RUN pip install google-api-core google-auth google-cloud-compute googleapis-common-protos 

RUN pip install azure-common azure-core azure-identity azure-mgmt-compute azure-mgmt-core azure-mgmt-network azure-mgmt-resource

RUN pip install cockroachdb-cloud-client

USER 1000


# docker build -t fabiog1901/awx-ee:latest .
# docker push fabiog1901/awx-ee:latest
