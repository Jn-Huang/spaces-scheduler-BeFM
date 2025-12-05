# BeFM Space Scheduler

[![Resume Hugging Face Space (8am Eastern)](https://github.com/Jn-Huang/spaces-scheduler-BeFM/actions/workflows/resume_space.yaml/badge.svg)](https://github.com/Jn-Huang/spaces-scheduler-BeFM/actions/workflows/resume_space.yaml)

This repository controls the scheduling for the [BeFM Hugging Face Space](https://huggingface.co/spaces/JinHuang1203/BeFM).

**Paper:** [https://arxiv.org/abs/2505.23058](https://arxiv.org/abs/2505.23058)

The scheduler uses [GitHub Actions](https://docs.github.com/en/actions) to automatically start the Space at 8am ET on weekdays.

# Usage

Follow these instructions to schedule automated rebuilds of your Hugging Face Space. You need to update the repository to point to the target Space and provide a Hugging Face `write` token.

1. To get started, fork or clone this repository to your own GitHub account.
2. Navigate to `/restart_space.py`.
3. Refer to `restart_space()` function:

```python
def restart_space():
    token = os.environ['HF_TOKEN'] # Please navigate to Settings > Secrets and variables > Actions and define "HF_TOKEN".
    repo_id = "DIBT-Russian/MPEP_Dashboard" #  Please replace this value with the name of your own Hugging Face Space.
```

4. Modify `DIBT-Russian/MPEP_Dashbaord` to point to your Hugging Face Space using the syntax `{USER OR ORGANIZATION}/{SPACE}`.
5. In the Repository Menu, follow the path `Settings > Secrets and keys > Actions`.
6. On the Secrets tab, click New repository secret.
7. Create a new repository secret called `HF_KEY`.
8. Provide a [Hugging Face token](https://huggingface.co/settings/tokens) with `write` access from the account which owns the target Space.
9. Navigate to `/.github/workflows/restart_hf_space.yaml`.
10. Refer to `cron` schedule: `*/30 * * * *` and update it to your desired value. Please note, inducing rebuild too frequently can result in errored builds caused by compute throttling from Hugging Face. On a free-tier Gradio Space, schedule `*/10 * * * *` proved to be too frequent and hanging builds were observed.
11. Commit your changes and that's it! Your rebuild scheduler is ready to go!
