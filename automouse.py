import pyautogui
import time

# --- 1단계: 여기에 좌표 리스트를 붙여넣으세요 ---
# get_coords.py를 실행하여 얻은 좌표 리스트입니다.
coordinates = [
    (724, 574),
    (1411, 489),
    (1455, 197),
    (588, 175),
    (567, 554),
]

# ----------------------------------------------

print("="*50)
print(f"{len(coordinates)}개의 좌표를 순서대로 클릭합니다.")
print("3초 후에 시작합니다...")
print("="*50)
time.sleep(3)

# 저장된 좌표를 하나씩 순회하며 클릭
for i, coord in enumerate(coordinates):
    print(f"[{i+1}/{len(coordinates)}] {coord} 위치로 이동하여 클릭합니다.")
    pyautogui.click(coord)
    time.sleep(1) # 각 클릭 사이의 대기 시간

print("\n자동화 작업이 완료되었습니다.")
