import pyautogui
import time
import sys

# 좌표 설정 (본인 환경에 맞게 수정)
coordinates = [
    (1393, 650),  # 첫 번째 클릭 위치
    (338, 446),   # 두 번째 클릭 위치
]

print("=" * 50)
print("⌛ 3분마다 자동화를 무한 반복합니다.")
print("🖱 마우스를 절대 움직이지 마세요.")
print("3초 후에 시작합니다...")
print("=" * 50)
time.sleep(3)

try:
    while True:

        start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n🔁 {start_time} - 자동화 작업 시작")

        # 1. 첫 번째 좌표 클릭
        x1, y1 = coordinates[0]
        pyautogui.click(x1, y1)
        print(f"✅ 첫 번째 클릭: ({x1}, {y1})")
        time.sleep(1)

        # 4. Enter 입력
        pyautogui.press('enter')
        print("✅ Enter 입력")
        time.sleep(1)

        # 3. 붙여넣기 (⌘ + V)
        pyautogui.hotkey('command', 'v')
        print("✅ 붙여넣기 실행")
        time.sleep(1)

        # 4. Enter 입력
        pyautogui.press('enter')
        print("✅ Enter 입력")
        time.sleep(1)

        # 5. Esc 입력
        pyautogui.press('esc')
        print("✅ Esc 입력")
        time.sleep(1)

        print("⏳ 1분 대기 중...\n")

        # 3분 동안 매초 마우스 감지
        for _ in range(90):  # 3분 = 180초
            
            time.sleep(1)

except KeyboardInterrupt:
    print("⛔ 수동 종료되었습니다.")
