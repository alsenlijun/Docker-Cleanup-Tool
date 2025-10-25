import argparse
import subprocess

def run(cmd):
    print(f"> {cmd}")
    subprocess.call(cmd, shell=True)

def cleanup(dry_run):
    containers = "`docker ps -aq`"
    images = "`docker images -f dangling=true -q`"
    volumes = "`docker volume ls -qf dangling=true`"

    if dry_run:
        print("Dry run mode: showing what would be removed")
        run(f"docker ps -aq")
        run(f"docker images -f dangling=true -q")
        run(f"docker volume ls -qf dangling=true")
    else:
        run(f"docker rm {containers}")
        run(f"docker rmi {images}")
        run(f"docker volume rm {volumes}")
        print("Cleanup complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Show what will be removed")
    parser.add_argument("--force", action="store_true", help="Actually remove resources")
    args = parser.parse_args()

    if args.force:
        cleanup(dry_run=False)
    else:
        cleanup(dry_run=True)
