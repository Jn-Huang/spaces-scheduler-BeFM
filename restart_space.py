from huggingface_hub import HfApi
import os

def restart_space():
    token = os.environ['HF_TOKEN'] # Please navigate to Settings > Secrets and variables > Actions and define "HF_TOKEN".
    repo_id = "JinHuang1203/BeFM"  # Your Hugging Face Space

    try:
        api = HfApi(token=token)

        # Check if space is already running
        runtime = api.get_space_runtime(repo_id=repo_id)
        if runtime.stage == "RUNNING":
            print(f"Space {repo_id} is already running. Skipping restart.")
            return

        print(f"Space status: {runtime.stage}. Attempting to restart...")
        api.restart_space(repo_id=repo_id)
        print(f"Successfully restarted Space: {repo_id}")
    except Exception as e:
        print(f"Failed to restart Space {repo_id}: {e}")

if __name__ == "__main__":
    restart_space()
