# 📄 PDF Chatbot

A production-ready AI-powered PDF chatbot built with FastAPI, Pinecone, and RAG (Retrieval-Augmented Generation). Deployed on AWS EKS using Docker, GitHub Actions CI/CD pipeline.

---

## 🏗️ Architecture

```
User Request
     ↓
GitHub Actions (CI/CD)
     ↓
Docker Build → Amazon ECR
     ↓
AWS EKS (Kubernetes)
     ↓
EC2 Worker Nodes
     ↓
FastAPI Backend + Pinecone DB
```

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI (Python) |
| **Vector DB** | Pinecone |
| **AI/RAG** | LangChain + OpenAI |
| **Container** | Docker |
| **Registry** | Amazon ECR |
| **Orchestration** | Kubernetes (EKS) |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS (EC2, EKS, ECR) |

---

## 📁 Project Structure

```
pdf-chatbot/
├── backend/
│   ├── app.py              # Streamlit
│   ├── ingest.py           # PDF ingestion logic
│   ├── main.py             # FastAPI application
│   ├── pinecone_db.py      # Pinecone vector DB
│   ├── rag.py              # RAG pipeline
│   └── requirements.txt    # Python dependencies
├── k8s/
│   ├── deployment.yaml     # Kubernetes deployment
│   ├── service.yaml        # Kubernetes service
│   ├── configmap.yaml      # App configuration
│   └── secret.yaml         # Sensitive credentials
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions CI/CD
├── Dockerfile              # Docker image build
├── docker-compose.yml      # Local development
├── .gitignore
└── README.md
```

---

## ⚙️ Prerequisites

- Python 3.11+
- Docker Desktop
- AWS CLI
- kubectl
- eksctl
- Git

---

## 🔧 Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/pdf-chatbot.git
cd pdf-chatbot
```

### 2. Create .env File
```bash
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=us-east-1
OPENAI_API_KEY=your_openai_api_key
APP_ENV=development
PORT=8000
```

### 3. Run with Docker Compose
```bash
docker-compose up --build
```

### 4. Access API
```
http://localhost:8000
http://localhost:8000/docs  ← Swagger UI
```

---

## ☁️ AWS Setup

### 1. Configure AWS CLI
```bash
aws configure
# Enter Access Key ID, Secret Key, Region: us-east-1
```

### 2. Create ECR Repository
```bash
aws ecr create-repository --repository-name pdf-chatbot --region us-east-1
```

### 3. Create EKS Cluster
```bash
eksctl create cluster \
  --name pdf-chatbot-cluster \
  --region us-east-1 \
  --nodegroup-name workers \
  --node-type t2.micro \
  --nodes 1 \
  --nodes-min 1 \
  --nodes-max 1 \
  --managed
```

---

## 🔑 GitHub Secrets Required

Go to: `GitHub Repo → Settings → Secrets → Actions`

| Secret Name | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS IAM Access Key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM Secret Key |
| `AWS_REGION` | us-east-1 |
| `ECR_REGISTRY` | AWS ECR Registry URL |
| `ECR_REPOSITORY` | pdf-chatbot |
| `PINECONE_API_KEY` | Pinecone API Key |
| `OPENAI_API_KEY` | OpenAI API Key |

---

## 🔄 CI/CD Pipeline

Every push to `main` branch triggers:

```
Push to main
     ↓
GitHub Actions starts
     ↓
Configure AWS credentials
     ↓
Login to Amazon ECR
     ↓
Docker build & push image
     ↓
Update kubeconfig (EKS)
     ↓
Apply Kubernetes manifests
     ↓
Rolling deployment restart
     ↓
✅ App live on EKS!
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/upload` | Upload PDF file |
| `POST` | `/chat` | Chat with PDF |
| `GET` | `/docs` | Swagger UI |

---

## 🌐 Deployment

### Get Live URL
```bash
kubectl get services

# Output:
# NAME                  TYPE           EXTERNAL-IP
# pdf-chatbot-service   LoadBalancer   abc123.us-east-1.elb.amazonaws.com
```

Your app is live at:
```
http://abc123.us-east-1.elb.amazonaws.com
```

---

## 💰 AWS Cost Estimate

| Service | Cost/Month |
|---|---|
| EKS Cluster | ~$73 |
| EC2 t2.micro | ~$8 |
| ECR Storage | ~$1 |
| Load Balancer | ~$18 |
| **Total** | **~$100/month** |

> 💡 Stop cluster when not in use to save costs

---

## 🛑 Stop/Delete Cluster

```bash
# Delete cluster (stop billing)
eksctl delete cluster --region=us-east-1 --name=pdf-chatbot-cluster
```

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 👤 Author

**Ankur**
- GitHub: https://github.com/Ankurgharde

---

⭐ Star this repo if you found it helpful!
