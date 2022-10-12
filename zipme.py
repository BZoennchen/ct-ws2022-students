# Mit diesem Skript können Sie sich das den aktuelle Ordner in eine Datei zusammepacken.
# Diese können Sie anschließend herunterladen.

import subprocess
from pathlib import Path

if __name__ == "__main__":
    tar_file = 'archive.tar.gz'
    path = Path(tar_file)
    
    if not path.is_file():
        process = subprocess.run(f'touch {tar_file}'.split(' '))
    
    process = subprocess.run(f'tar --exclude={tar_file} --exclude=zipme.py -czf {tar_file} .'.split(' '))
    if not process.check_returncode():
        print(f'Der Inhalt dieses Ordners wurde in {tar_file} gepackt.\nSie können diese Datei nun herunterladen.\nDie Datei kann z.B. mit dem Programm GZip oder 7zip (Windows) geöffnet/entpackt werden.')