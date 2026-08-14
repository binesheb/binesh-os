# Getting Started — Raspberry Pi

B.I.N.E.S.H. OS can run as a native Linux service or in Docker.

## Native

```bash
sudo apt update
sudo apt install -y python3 python3-venv git
python3 -m venv .venv
source .venv/bin/activate
pip install -r platforms/raspberry-pi/requirements.txt
python platforms/raspberry-pi/main.py
```

## Docker

```bash
docker compose up --build
```

The Linux runtime is intended for edge gateway, local API, synchronization, storage and automation workloads.
