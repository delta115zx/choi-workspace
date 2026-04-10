import olefile
import os
import sys

# 1. 파일 이름 (확장자까지 정확히)
hwp_file_name = "식품영업등록신청서.hwp" 

def get_hwp_text(filename):
    # ⭐ 핵심: 현재 실행 중인 파이썬 스크립트(.py)의 실제 폴더 경로를 가져옵니다.
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    
    # 그 폴더 경로와 파일 이름을 합칩니다.
    full_path = os.path.join(current_script_path, filename)
    
    print(f"--- 경로 확인 ---")
    print(f"스크립트 위치: {current_script_path}")
    print(f"찾으려는 전체 경로: {full_path}")
    print(f"------------------")

    if not os.path.exists(full_path):
        print(f"❌ 에러: [{full_path}] 경로에 파일이 없습니다.")
        print("💡 팁: '식품영업등록신청서.hwp' 파일이 'Mar03_03' 폴더 안에 있는지 확인해주세요.")
        return None

    try:
        f = olefile.OleFileIO(full_path)
        if f.exists('PrvText'):
            data = f.openstream('PrvText').read()
            return data.decode('utf-16')
        else:
            print("⚠️ 경고: 파일은 찾았으나 텍스트 섹션이 없습니다. (서식만 있는 파일일 수 있음)")
            return None
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return None

# 실행
text_result = get_hwp_text(hwp_file_name)

if text_result:
    # 저장 경로도 파이썬 파일과 같은 위치로 지정
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hwp_result.txt")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text_result)
    print(f"✅ 성공! 결과가 저장되었습니다: {save_path}")