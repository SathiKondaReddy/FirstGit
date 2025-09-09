import os

print(f"Failed ECR Dockerfiles: {os.getenv("FAILED_ECR_DOCKERFILES")}")
print(f"Failed ACR Dockerfiles: {os.getenv("FAILED_ACR_DOCKERFILES")}")
