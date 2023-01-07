import os, subprocess
import requests
from zipfile import ZipFile

try:
    xenia_zip_file = "xenia_canary_latest.zip"

    version_file = open("version.txt", "a+")
    version_file.close()

    response = requests.get("https://api.github.com/repos/xenia-canary/xenia-canary/releases/latest")

    current_version = str(response.json()["id"])
    if open("version.txt", "r").read() != (current_version):
        response = requests.get("https://github.com/xenia-canary/xenia-canary/releases/download/experimental/xenia_canary.zip")
        open(xenia_zip_file, "wb").write(response.content)

        with ZipFile(xenia_zip_file) as xenia_latest_zip_file:
            xenia_latest_zip_file.extractall(path ="../")

        version_file = open("version.txt", "w")
        version_file.write(current_version)
        version_file.close()

    import os
    if os.path.exists(xenia_zip_file):
        os.remove(xenia_zip_file)

    subprocess.call("xenia_canary.exe")
except:
    subprocess.call("xenia_canary.exe")