# AWX CockroachDB

Project for Ansible AWX integration

## Demo

```text
$ minikube config view
- cpus: 8
- driver: hyperkit
- memory: 24000


$ minikube profile list
|---------|-----------|---------|---------------|------|---------|---------|-------|--------|
| Profile | VM Driver | Runtime |      IP       | Port | Version | Status  | Nodes | Active |
|---------|-----------|---------|---------------|------|---------|---------|-------|--------|
| awx     | hyperkit  | docker  | 192.168.64.16 | 8443 | v1.26.1 | Running |     1 |        |
|---------|-----------|---------|---------------|------|---------|---------|-------|--------|

$ minikube profile awx
✅  minikube profile was successfully set to awx


$ minikube start
😄  [awx] minikube v1.30.1 on Darwin 13.3.1
🆕  Kubernetes 1.26.3 is now available. If you would like to upgrade, specify: --kubernetes-version=v1.26.3
✨  Using the hyperkit driver based on existing profile
👍  Starting control plane node awx in cluster awx
🔄  Restarting existing hyperkit VM for "awx" ...
❗  Image was not built for the current minikube version. To resolve this you can delete and recreate your minikube cluster using the latest images. Expected minikube version: v1.29.0 -> Actual minikube version: v1.30.1
🐳  Preparing Kubernetes v1.26.1 on Docker 20.10.23 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
    ▪ Using image docker.io/kubernetesui/dashboard:v2.7.0
    ▪ Using image docker.io/kubernetesui/metrics-scraper:v1.0.8
💡  Some dashboard features require the metrics-server addon. To enable all features please run:

        minikube -p awx addons enable metrics-server


🌟  Enabled addons: storage-provisioner, default-storageclass, dashboard
🏄  Done! kubectl is now configured to use "awx" cluster and "default" namespace by default


$ minikube service list -n awx
|-----------|-------------------------------------------------|--------------|----------------------------|
| NAMESPACE |                      NAME                       | TARGET PORT  |            URL             |
|-----------|-------------------------------------------------|--------------|----------------------------|
| awx       | awx-demo-postgres                               | No node port |                            |
| awx       | awx-demo-service                                | http/80      | http://192.168.64.16:30080 |
| awx       | awx-operator-controller-manager-metrics-service | No node port |                            |
|-----------|-------------------------------------------------|--------------|----------------------------|


$ minikube dashboard
🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:50215/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...




$ kubectl config set-context --current --namespace=awx

$ k config get-contexts
CURRENT   NAME   CLUSTER   AUTHINFO   NAMESPACE
*         awx    awx       awx        awx
```
