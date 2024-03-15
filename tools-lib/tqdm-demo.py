from tqdm import tqdm
from time import sleep

for i in tqdm(
    range(80), desc="Loading... (ascii=False, ncols=75)", ascii=False, ncols=80
):
    sleep(0.05)

for i in tqdm(
    range(80), desc="Loading... (ascii=True, ncols=20)", ascii=True, ncols=120
):
    sleep(0.05)

for i in tqdm(
    range(80),
    desc="Loading... (fullwide default)",
):
    sleep(0.05)

print("Complete.")
