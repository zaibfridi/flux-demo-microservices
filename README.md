# flux-demo-microservices
cd backend
docker build -t zaibfridi/backend:0.1.1 .
docker build -t zaibfridi/backend:0.1.2 .

helm install backend --dry-run --debug backend/helm/backend


helm install backend backend/helm/backend


helm upgrade backend backend/helm/backend