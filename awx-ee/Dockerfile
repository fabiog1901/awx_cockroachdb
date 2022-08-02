FROM quay.io/ansible/awx-ee:latest
USER root

# add Python dependencies and Ansible
# Galary dependencies
ADD requirements.yml /tmp/requirements.yml

# upgrade pip
RUN /usr/bin/python3 -m pip install --upgrade pip

# install Ansible Galaxy collections
# RUN ansible-galaxy collection install git+https://github.com/fabiog1901/cockroachdb-collection.git
RUN ansible-galaxy collection install ansible.posix
RUN ansible-galaxy collection install community.general

# install Python dependencies
RUN pip install boto3 boto botocore google-api-core google-auth google-cloud-compute googleapis-common-protos azure-common azure-core azure-identity azure-mgmt-compute azure-mgmt-core azure-mgmt-network azure-mgmt-resource

RUN rpm --import https://packages.microsoft.com/keys/microsoft.asc
RUN dnf install -y https://packages.microsoft.com/config/rhel/8/packages-microsoft-prod.rpm
RUN dnf update
RUN dnf install -y azure-cli

USER 1000


# docker build -t fabiog1901/fab-ee:latest
# docker push fabiog1901/fab-ee:latest

