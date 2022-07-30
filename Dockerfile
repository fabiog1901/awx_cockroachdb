FROM ubuntu:latest

RUN apt update

RUN apt install -y python3 python3-pip git curl wget vim

RUN pip install boto3 boto botocore

