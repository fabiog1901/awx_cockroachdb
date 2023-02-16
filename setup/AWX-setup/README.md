# CockroachDB for AWX

```bash
# minikube
minikube start -p awx

# install with the operator 
# https://github.com/ansible/awx-operator

kubectl get pods -n awx
kubectl config set-context --current --namespace=awx

# in a new terminal launch the dashboard
minikube dashboard -p awx

# AWX URL
minikube service awx-demo-service --url -n awx -p awx

# password for user admin
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" -n awx | base64 --decode

```
