from huggingface_hub import HfApi
import os

def pause_space():
    token = os.environ['HF_TOKEN']
    repo_id = "befm/BeFM"  # Your Hugging Face Space

    try:
        HfApi().pause_space(repo_id=repo_id, token=token)
        print(f"Successfully paused Space: {repo_id}")
    except Exception as e:
        print(f"Failed to pause Space {repo_id}: {e}")

if __name__ == "__main__":
    pause_space()
