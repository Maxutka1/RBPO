import subprocess
import logging
import os

logging.basicConfig(level=logging.INFO)

password = os.environ.get("PBX_PASSWORD")
if not password:
    logging.error("PBX_PASSWORD environment variable not set")
else:
    logging.info("Connecting to PBX using credentials from env")

def get_call_log(phone_number):
    result = subprocess.run(
        ["tail", "-n", "100", "/var/log/asterisk/cdr.csv"],
        capture_output=True,
        text=True
    )
    lines = result.stdout.splitlines()
    filtered = [line for line in lines if phone_number in line]
    return "\n".join(filtered)
