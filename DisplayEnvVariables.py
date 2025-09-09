import os

print(f"Failed ECR Dockerfiles: {os.getenv("FAILED_ECR_DOCKERFILES")}")
print(f"TYPE ECR Dockerfiles: {type(os.getenv("FAILED_ECR_DOCKERFILES"))}")

print(f"Failed ACR Dockerfiles: {os.getenv("FAILED_ACR_DOCKERFILES")}")
print(f"TYPE ACR Dockerfiles: {type(os.getenv("FAILED_ACR_DOCKERFILES"))}")

print(f"===================================================================")

failed_ecr = os.getenv("FAILED_ECR_DOCKERFILES", "")
failed_acr = os.getenv("FAILED_ACR_DOCKERFILES", "")

list_ecr = failed_ecr.split()
list_acr = failed_acr.split()

combined = sorted(set(list_ecr + list_acr))

if combined:
    print("🚨 Overall Failed Dockerfiles:")
    for item in combined:
        print(f" - {item}")
    print(f"📦 Total unique failures: {len(combined)}")
else:
    print("✅ No failures detected.")
