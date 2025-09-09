import os

print(f"Failed ECR Dockerfiles: {os.getenv("FAILED_ECR_DOCKERFILES")}")
print(f"TYPE ECR Dockerfiles: {type(os.getenv("FAILED_ECR_DOCKERFILES"))}")

print(f"Failed ACR Dockerfiles: {os.getenv("FAILED_ACR_DOCKERFILES")}")
print(f"TYPE ACR Dockerfiles: {type(os.getenv("FAILED_ACR_DOCKERFILES"))}")

print(f"===================================================================")

# Get the env variables (space-separated or comma-separated)
failed_ecr = os.getenv("FAILED_ECR_DOCKERFILES", "")
failed_acr = os.getenv("FAILED_ACR_DOCKERFILES", "")

# Split into lists (adjust separator if needed)
list_ecr = failed_ecr.strip().split()
list_acr = failed_acr.strip().split()

# Merge and deduplicate
combined = list(set(list_ecr + list_acr))

# Print results
print("🚨 Combined Failed Dockerfiles:")
for item in sorted(combined):
    print(f" - {item}")

print(f"📦 Total unique failures: {len(combined)}")
