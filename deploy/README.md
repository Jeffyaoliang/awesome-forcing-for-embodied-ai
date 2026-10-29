# OpenReviewer-8B deployment

**Status: deployment files prepared, not a live deployment.** No user GPU has been provisioned from this conversation.

Official [model](https://huggingface.co/maxidl/Llama-OpenReviewer-8B) and [source](https://github.com/maxidl/openreviewer). Model weights ~16.1 GB, Llama 3.1 license and Meta terms apply. Official model supports vLLM.

## Prerequisites

A Linux NVIDIA CUDA machine (one H100 80GB recommended), GPU-compatible Docker and NVIDIA Container Toolkit; Hugging Face model access when required. The configured 8192-token maximum is intentionally shorter than the model's 128k training context, to conserve VRAM. The client truncates to 22,000 characters, so longer papers need sectional review.

## On the GPU host

```bash
docker compose -f deploy/docker-compose.yml up -d
curl -f http://127.0.0.1:8000/v1/models
python scripts/review_openreviewer.py path/to/paper.txt --out reviews/openreviewer-draft.md
```

Service listens on localhost only. Use SSH tunneling for a remote client. Do not expose an unauthenticated inference endpoint to the public Internet or commit private manuscripts/secrets.

The input is extracted UTF-8 paper text, not a PDF. This is a minimal model endpoint and client, **not** the official full PDF parsing workflow. It creates an unverified AI draft, not a peer-reviewed verdict. No real model execution or weight loading has occurred during this configuration step.
