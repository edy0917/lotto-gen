import requests
import os
import datetime

def get_twitter_keywords():
    # 실제 구현 시 여기서 트위터 글을 수집하여 키워드만 추출합니다.
    # 글로벌 수익형 웹을 위해 영어 키워드로 변환하는 과정이 포함됩니다.
    return "Cyberpunk city, neon lights, high tech, futuristic skyscraper, solar panels"

def generate_ai_image(prompt):
    print(f"이미지 생성 중: {prompt}")
    
    # Pollinations AI를 사용하여 무료로 이미지 생성 (API 키 불필요)
    # 이미지 사이즈는 글로벌 규격인 1080x1080으로 설정
    encoded_prompt = requests.utils.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1080&nologo=true"
    
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            if not os.path.exists('images'):
                os.makedirs('images')
            
            with open('images/today_summary.png', 'wb') as f:
                f.write(response.content)
            print("순수 AI 이미지 생성 및 저장 완료!")
        else:
            print("이미지 생성 실패")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    # 1. 트위터 키워드 가져오기
    keywords = get_twitter_keywords()
    
    # 2. 키워드 기반 이미지 생성
    generate_ai_image(keywords)
