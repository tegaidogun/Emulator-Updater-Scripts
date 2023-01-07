import os, subprocess
import requests
from zipfile import ZipFile

try:
    cxbx_zip_file = "cxbx_reloaded_latest.zip"

    version_file = open("version.txt", "a+")
    version_file.close()

    response = requests.get("https://api.github.com/repos/Cxbx-Reloaded/Cxbx-Reloaded/releases")

    current_version = str(response.json()[0]["id"])
    if open("version.txt", "r").read() != (current_version):
        response = requests.get(requests.get("https://api.github.com/repos/Cxbx-Reloaded/Cxbx-Reloaded/releases").json()[0]["assets"]["browser_download_url"])
        open(cxbx_zip_file, "wb").write(response.content)

        with ZipFile(cxbx_zip_file) as extracting_cxbx_file:
            extracting_cxbx_file.extractall()

        version_file = open("version.txt", "w")
        version_file.write(current_version)
        version_file.close()

    if os.path.exists(cxbx_zip_file):
        os.remove(cxbx_zip_file)

    subprocess.call("cxbx.exe")
except:
    subprocess.call("cxbx.exe")