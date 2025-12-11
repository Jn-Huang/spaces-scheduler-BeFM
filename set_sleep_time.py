from huggingface_hub import HfApi
import os
import sys

def set_sleep_time(sleep_seconds):
    token = os.environ['HF_TOKEN']
    repo_id = "befm/BeFM"  # Your Hugging Face Space

    try:
        HfApi().set_space_sleep_time(repo_id=repo_id, sleep_time=sleep_seconds, token=token)
        print(f"Successfully set sleep time to {sleep_seconds} seconds ({sleep_seconds/3600:.1f} hours) for Space: {repo_id}")
    except Exception as e:
        print(f"Failed to set sleep time for Space {repo_id}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python set_sleep_time.py <sleep_seconds>")
        sys.exit(1)

    sleep_seconds = int(sys.argv[1])
    set_sleep_time(sleep_seconds)
