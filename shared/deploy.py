import subprocess
import sys


def run(*args: str) -> None:
    subprocess.run(["platformctl", *args], check=True)


# --8<-- [start:main]
def main(service: str, version: str) -> None:
    run("deploy", "--service", service, "--version", version)
    run("status", "--service", service)
# --8<-- [end:main]


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
