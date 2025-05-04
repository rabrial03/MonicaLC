import requests, zipfile, os, shutil, glob, yara

def create(folder):
        if not os.path.exists(folder):
                os.mkdir(folder)

def copyfiles(src, dst):
        for root, dirs, files in os.walk(src):
            for filename in files:
                if ('.yara' in filename or '.yar' in filename):
                    shutil.copy(os.path.join(root, filename), os.path.join(dst, filename))

def unzip(filename, dst):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(dst)

def download(dst, path):
    r = requests.get(path)
    open(dst, 'wb').write(r.content)

def compile(filepaths, save_folder):
    compiled_rules = dict()
    for folder in filepaths:
        for filename in glob.glob(folder + '/*.yar*'):
            namespace = os.path.basename(os.path.splitext(filename)[0])
            compiled_rules[namespace] = filename
    rules = yara.compile(filepaths = compiled_rules)
    print(compiled_rules)
    if os.path.exists(save_folder):
        os.remove(save_folder)
    rules.save(save_folder)

root = os.path.dirname(os.path.abspath(__file__))
compiled_rules = os.path.join(root, "reglas_yara", "rules-compiled")

# Zip filename
cape_filename = os.path.join(root, 'CAPEv2.zip')
reversinglabs_filename = os.path.join(root, 'reversinglabs-yara-rules-develop.zip')

# Folder unzip
capev2_folder = os.path.join(root, 'CAPEv2-master')
yara_cape_folder = os.path.join(root, 'CAPEv2-master', 'data', 'yara', 'CAPE')
reversinglab_folder = os.path.join(root, 'reversinglabs-yara-rules-develop')
yara_reversinglab_folder = os.path.join(root, 'reversinglabs-yara-rules-develop', 'yara')

# Local folders
local_cape_folder = os.path.join(root, 'reglas_yara', 'Cape')
local_reversinglabs_folder = os.path.join(root, 'reglas_yara', 'ReversingLabs')
local_neo23x0_folder = os.path.join(root, 'reglas_yara', 'Neo23x0')
local_threathunting_folder = os.path.join(root, 'reglas_yara', 'ThreatHunting')

# Directories to compile (added Neo23x0 and ThreatHunting)
directories = [local_cape_folder, local_reversinglabs_folder, local_neo23x0_folder, local_threathunting_folder]

# CAPEv2
create(folder=local_cape_folder)
download(dst=cape_filename, path='https://codeload.github.com/kevoreilly/CAPEv2/zip/refs/heads/master')
unzip(filename=cape_filename, dst=root)
shutil.copytree(src=yara_cape_folder, dst=local_cape_folder, dirs_exist_ok=True)
shutil.rmtree(capev2_folder)
os.remove(cape_filename)

# ReversingLabs
create(folder=local_reversinglabs_folder)
download(dst=reversinglabs_filename, path='https://codeload.github.com/reversinglabs/reversinglabs-yara-rules/zip/refs/heads/develop')
unzip(filename=reversinglabs_filename, dst=root)
copyfiles(src=yara_reversinglab_folder, dst=local_reversinglabs_folder)
shutil.rmtree(reversinglab_folder)
os.remove(reversinglabs_filename)

# Neo23x0 and ThreatHunting (you'll need to copy the YARA rules manually into these folders)
# If the YARA rules are already manually placed in the folders, you can skip the download and unzip steps for them.

create(folder=local_neo23x0_folder)
create(folder=local_threathunting_folder)
# Assuming you have copied the YARA rules into these folders, the following code will simply include them in the compilation.

# Compile all directories
compile(filepaths=directories, save_folder=compiled_rules)
