# Docker Cleanup Tool

A simple DevOps productivity utility to automatically clean up unused Docker containers, images, and volumes.

## Features
- Remove stopped containers
- Remove dangling images
- Remove unused volumes
- Safe mode (dry-run) support

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python src/cleanup.py --dry-run
python src/cleanup.py --force
```

