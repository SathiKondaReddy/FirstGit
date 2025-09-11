import os

def DisplaySomething(message: str):

    print(message)

    print(f"Failed ECR Dockerfiles: {os.getenv("FAILED_ECR_DOCKERFILES")}")
    print(f"TYPE ECR Dockerfiles: {type(os.getenv("FAILED_ECR_DOCKERFILES"))}")

    print(f"Failed ACR Dockerfiles: {os.getenv("FAILED_ACR_DOCKERFILES")}")
    print(f"TYPE ACR Dockerfiles: {type(os.getenv("FAILED_ACR_DOCKERFILES"))}")

    print(f"===================================================================")

    failed_ecr = os.getenv("FAILED_ECR_DOCKERFILES", "").split()
    failed_acr = os.getenv("FAILED_ACR_DOCKERFILES", "").split()

    combined = sorted(set(failed_ecr + failed_acr))

    if combined:
        print("🚨 Overall Failed Dockerfiles:")
        for item in combined:
            print(f" - {item}")
        print(f"📦 Total unique failures: {len(combined)}")
    else:
        print("✅ No failures detected.")
