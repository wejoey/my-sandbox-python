#!/usr/bin/python
import os
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

input_files_recursion = "~/.config ~/.local/bin"
input_files_no_recursion = (
    "~/.* ~/* ~/.cargo/.* ~/.cargo/* ~/.rustup/* ~/.vcpkg/* /etc/wsl.conf"
)
output_file = f"~/{current_date}-WSL-bkp.tar"

print(f"Backup of {input_files_recursion} with recursion...")
print(f"Backup of {input_files_no_recursion} with no_recursion...")

os.system(f"tar -cvf {output_file} {input_files_recursion}")
os.system(f"tar --append --no-recursion -vf {output_file} {input_files_no_recursion}")

os.system(f"gzip {output_file}")

output_file_compressed = f"{output_file}.gz"
