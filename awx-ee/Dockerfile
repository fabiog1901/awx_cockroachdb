FROM quay.io/ansible/awx-ee:latest
USER root

# add Python dependencies and Ansible
# Galary dependencies
ADD requirements.yml /tmp/requirements.yml

# upgrade pip
RUN /usr/bin/python3 -m pip install --upgrade pip

# install Ansible Galaxy collections
RUN ansible-galaxy collection install -r /tmp/requirements.yml --collections-path /usr/share/ansible/collections

# install Python dependencies
RUN pip install boto3 boto botocore google-api-core google-auth google-cloud-compute googleapis-common-protos azure-common azure-core azure-identity azure-mgmt-compute azure-mgmt-core azure-mgmt-network azure-mgmt-resource


USER 1000


# docker build -t fabiog1901/fab-ee:latest
# docker push fabiog1901/fab-ee:latest

