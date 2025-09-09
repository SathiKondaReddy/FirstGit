import os

failed_ecr_dockerfiles = []
failed_acr_dockerfiles = []

failed_ecr_dockerfiles.append("base_images/image1.Dockerfile")
failed_ecr_dockerfiles.append("base_images/image2.Dockerfile")

print(f"Failed ECR Dockerfiles: {failed_ecr_dockerfiles}")
print(f"Type: {type(failed_ecr_dockerfiles)}")


env_file = os.getenv('GITHUB_ENV')
with open(env_file, "a") as gh_environment:
    gh_environment.write(f"FAILED_ECR_DOCKERFILES={failed_ecr_dockerfiles}\n")
    gh_environment.write(f"FAILED_ACR_DOCKERFILES={failed_acr_dockerfiles}\n")