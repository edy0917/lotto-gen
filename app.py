import requests
import os

def generate_ai_image():
    # 1. 키워드 설정 (글로벌 타겟을 위해 영어로만 구성)
    # 텍스트를 배제하기 위해 'no text, no letters' 문구를 추가했습니다.
    prompt = "futuristic cyber city, cinematic lighting, 8k, highly detailed, no text, no letters"
    
    print(f"Generating image for: {prompt}")
    
    encoded_prompt = requests.utils.quote(prompt)
    # nologo=true 옵션으로 깔끔한 이미지만 가져옵니다.
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed=42"
    
    try:
        response = requests.get(image_url, timeout=30)
        if response.status_code == 200:
            if not os.path.exists('images'):
                os.makedirs('images')
            
            with open('images/today_summary.png', 'wb') as f:
                f.write(response.content)
            print("성공: images/today_summary.png 저장 완료")
        else:
            print(f"실패: 상태 코드 {response.status_code}")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    generate_ai_image()
