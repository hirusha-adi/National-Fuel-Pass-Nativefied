import os
import shutil


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')


_clear()
CWD = os.getcwd()
dist_folder = os.path.join(CWD, 'dist')
icon_file_full = os.path.join(CWD, 'icon.co')
if not(os.path.isdir(dist_folder)):
    os.makedirs(dist_folder)
if not(os.path.isfile(icon_file_full)):
    try:
        import requests
    except ImportError:
        os.system('py -m pip install requests' if os.name ==
                  'nt' else 'python3 -m pip install requests')
    r = requests.get("https://fuelpass.gov.lk/favicon-nfp.ico")
    with open(icon_file_full, 'wb') as _icon_file:
        _icon_file.write(r.content)

# Sample command -->
# nativefier.cmd 'fuelpass.gov.lk' --name "National Fuel Pass" --icon .\icon.ico --verbose --portable

# Normal Version
command_final_normal = ""
command_final_normal += "nativefier.cmd" if os.name == 'nt' else 'nativefier'
command_final_normal += " 'fuelpass.gov.lk'"
command_final_normal += ' --name "National Fuel Pass"'
command_final_normal += f' --icon "{icon_file_full}"'
command_final_normal += f' --verbose'
os.system(command_final_normal)
for folder in os.listdir(CWD):
    # National Fuel Pass-win32-x64
    if folder.startswith("National Fuel Pass"):
        folder_path_full_original = os.path.join(CWD, folder)
        folder_path_full_destination = os.path.join(dist_folder, folder)
        shutil.move(folder_path_full_original,
                    folder_path_full_destination)

# Portable Version
command_final_portable = command_final_normal + ' --portable'
os.system(command_final_normal)
for folder in os.listdir(CWD):
    if folder.startswith("National Fuel Pass"):
        folder_path_full_original = os.path.join(CWD, folder)
        # National Fuel Pass-win32-x64-Portable
        folder_path_full_destination = os.path.join(
            dist_folder, str(folder) + '-Portable')
        shutil.move(folder_path_full_original,
                    folder_path_full_destination)
