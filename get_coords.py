
import pyautogui
import time

positions = []
num_positions = 5

print("="*50)
print(f"{num_positions}개의 마우스 좌표를 기록합니다.")
print("="*50)

for i in range(num_positions):
    print(f"▶ {i+1}번째 위치로 5초 안에 마우스를 이동하세요...")
    time.sleep(5)
    pos = pyautogui.position()
    positions.append(pos)
    print(f"✅ {i+1}번째 좌표 저장 완료: {pos}")
    print("---"*10)

print("\n"*2)
print("="*50)
print("모든 좌표 기록이 완료되었습니다.")
print("아래 리스트를 복사하여 메인 스크립트에 사용하세요.")
print("="*50)

# 코드에 바로 붙여넣을 수 있는 형태로 출력
print("coordinates = [")
for pos in positions:
    print(f"    ({pos.x}, {pos.y}),")
print("]")
