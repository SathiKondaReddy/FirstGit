import os

print(f"Failed ECR Dockerfiles: {os.getenv("FAILED_ECR_DOCKERFILES")}")
print(f"TYPE ECR Dockerfiles: {type(os.getenv("FAILED_ECR_DOCKERFILES"))}")

print(f"Failed ACR Dockerfiles: {os.getenv("FAILED_ACR_DOCKERFILES")}")
print(f"TYPE ACR Dockerfiles: {type(os.getenv("FAILED_ACR_DOCKERFILES"))}")


