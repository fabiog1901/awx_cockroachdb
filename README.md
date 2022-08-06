# CockroachDB for AWX

```bash
# minikube
minikube start --cpus=4 --memory=6g --addons=ingress

kubectl get pods -n awx
kubectl config set-context --current --namespace=awx

# AWX URL
minikube service awx-demo-service --url -n awx

# password for user admin
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" -n awx | base64 --decode

```
