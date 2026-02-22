import requests
import os

def generate_ai_image():
    # 글로벌 유저를 위한 화려한 배경 프롬프트 (텍스트 제외 옵션 포함)
    prompt = "high-tech futuristic city, cinematic view, 8k wallpaper, no text, no lettering"
    print(f"이미지 생성 요청 중: {prompt}")
    
    encoded_prompt = requests.utils.quote(prompt)
    # Pollinations AI를 사용해 고퀄리티 이미지를 무료로 가져옵니다.
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1080&nologo=true"
    
    try:
        response = requests.get(image_url, timeout=30)
        if response.status_code == 200:
            if not os.path.exists('images'):
                os.makedirs('images')
            
            with open('images/today_summary.png', 'wb') as f:
                f.write(response.content)
            print("성공: 순수 AI 이미지가 images/today_summary.png에 저장되었습니다.")
        else:
            print(f"이미지 생성 실패 (코드: {response.status_code})")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    generate_ai_image()
