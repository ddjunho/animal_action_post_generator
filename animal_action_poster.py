import requests
import json
import random
import creds
import os
# 액세스 토큰을 가져오는 함수
def getLongLivedToken():
    url = "https://graph.facebook.com/v16.0/oauth/access_token?"
    url += "grant_type=fb_exchange_token&client_id=" + creds.getCreds()['client_id'] + "&client_secret=" + creds.getCreds()['client_secret'] + "&fb_exchange_token=" + getAccessToken()
    print(url)

def getPostUrl():
    return creds.getCreds()['post_url']

def getAccessToken():
    return creds.getCreds()['access_token']

def getInstagramID():
    return creds.getCreds()['instagram_business_account']

def getFacebookPageID():
    return creds.getCreds()['page_id']

# 게시할 이미지와 캡션에 대한 페이로드 생성
def payload_one_creator(image_url, caption):
    payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": getAccessToken()
    }
    return payload

def payload_two_creator(creation_id):
    payload = {
        "creation_id": creation_id,
        "access_token": getAccessToken()
    }
    return payload

# 이미지를 게시하는 함수
def postImage(image_url, caption):
    r = requests.post(getPostUrl(), data=payload_one_creator(image_url, caption))
    result = json.loads(r.text)
    if not "id" in result:
        print("There was an error posting the image.")
        print("Result : " + str(result))
        return
    
    creation_id = result["id"]
    print("Creation ID: " + creation_id)

    second_request_url = getPostUrl() + "_publish"
    second_payload = payload_two_creator(creation_id)
    r = requests.post(second_request_url, data=second_payload)

    print("Image posted successfully.")

# OpenAI API를 사용할 함수들
import openai

openai.api_key = creds.getCreds()['open_ai_key']
model = creds.getCreds()['model']

def use_chatGPT(prompt):
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "글로 구체적이고 시각적으로 생생한 묘사를 포함하는 것이 중요합니다. 이미지의 색상, 배경, 분위기, 구도, 인물의 특징 등을 생각해서 글로 예술적으로 표현해주세요. 질문 :"+prompt}]
    )
    return response.choices[0].message.content

def use_dallE(prompt):
    image = openai.images.generate(
        model="dall-e-3",
        prompt='I NEED to test how the tool works with extremely simple prompts. DO NOTadd any detail, just use it AS-IS:'+prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return image.data[0].url

# 사물 100가지 리스트
objects = [
    "책", "연필", "사과", "컵", "의자", "컴퓨터", "모자", "가방", "시계", "신문",
    "전구", "테이블", "나무", "사전", "사진기", "가위", "종이", "칼", "휴대폰", "헤드폰",
    "화분", "키보드", "마우스", "텀블러", "컵라면", "문서", "캔들", "탁자", "모니터", "의료기기",
    "스마트워치", "타자기", "조명", "종이접기", "나침반", "구두", "젓가락", "볼펜", "컵받침", "서랍",
    "선풍기", "청소기", "냉장고", "세탁기", "전자레인지", "그릇", "찻잔", "일기장", "종이컵", "스케치북",
    "수첩", "전화기", "스피커", "카메라", "배낭", "가습기", "벽시계", "톱", "송곳", "브로셔",
    "식탁", "컴퓨터 모니터", "비행기 모형", "치약", "면도기", "마스크", "이불", "베개", "텐트", "장갑",
    "스포츠 용품", "배", "그림", "퍼즐", "주전자", "화장지", "도어벨", "스톱워치", "사다리", "목걸이",
    "캘린더", "테이프", "우산", "미술 도구", "시계탑", "고무줄", "지우개", "브러시", "도장", "슬리퍼",
    "간식", "프레임", "라디오", "소화기", "상자", "다리미", "가위", "불펜", "포스트잇", "음악 플레이어"
]

# 동물 100가지 리스트
animals = [
    "고양이", "개", "코끼리", "사자", "호랑이", "곰", "여우", "늑대", "토끼", "사슴",
    "원숭이", "기린", "다람쥐", "너구리", "오리", "펭귄", "악어", "물개", "해파리", "말",
    "고래", "상어", "구름다리", "메기", "참새", "독수리", "타조", "나비", "벌", "지렁이",
    "개미", "가재", "물고기", "코알라", "캥거루", "소", "돼지", "양", "거북이", "문어",
    "아기곰", "코뿔소", "하마", "말벌", "상어", "무당벌레", "쥐", "홍학", "메추리", "두더지",
    "여우", "재규어", "치타", "기린", "늑대", "개구리", "천둥소리", "악어", "여우", "키위",
    "팬더", "무스", "타조", "송아지", "오리너구리", "앵무새", "파리", "신기루", "호저", "원숭이",
    "사슴", "물소", "지렁이", "주머니쥐", "마카크", "햄스터", "키위", "다람쥐", "물떼새", "사막여우",
    "고릴라", "조개", "복어", "거북이", "상어", "민물고기", "스컹크", "수리부엉이", "비버", "산양",
    "오리", "지렁이", "물고기", "비둘기", "황새", "수달",
]

# 장소 리스트
places = [
    "버블룸", "화성", "미래 도시", "어드벤처 공원", "비밀 정원", "판타지 성", "스카이워크", 
    "시간 여행 카페", "수중 레스토랑", "동화 속 마을", "기계 정원", "별빛 아래", 
    "판타지 숲", "잊혀진 유적지", "오로라 아래", "안개 낀 언덕", "고대 피라미드", 
    "꿈의 섬", "마법의 숲", "우주 정거장", "비행선 위", "고대 성당", "요정의 숲", 
    "신비로운 해변", "공중 정원", "아이들이 그린 세상", "음악의 숲", "영화 촬영 현장", 
    "신화의 고향", "해양 생물 아쿠아리움", "빛의 축제", "화려한 카니발", "천상의 정원", 
    "무지개 다리", "겨울왕국", "고양이 카페", "레트로 게임방", "디지털 아트 갤러리", 
    "세계 정원", "빙하 언덕", "판타지 테마파크", "비밀의 연못", "바람의 동굴", 
    "천문 관측소", "초능력 훈련소", "로봇 카페", "엘프 마을", "자연 친화적인 스튜디오", 
    "고래 관찰소", "스팀펑크 거리", "외계인의 마을", "신비로운 지하 동굴", "아틀란티스"
]


# 동물 행동 리스트
actions = [
    "읽고 있다", "마시고 있다", "물고 있다", "밟고 있다", "앉아 있다", "숨쉬고 있다", "놀이하고 있다", 
    "돌보고 있다", "안고 있다", "유혹하고 있다", "잡고 있다", "빠르게 달리고 있다", "목욕하고 있다",
    "보호하고 있다", "노래하고 있다", "먹고 있다", "찾고 있다", "옮기고 있다", "들고 있다", "탐색하고 있다",
    "생각하고 있다", "그림 그리고 있다", "제작하고 있다", "장난치고 있다", "비추고 있다", "쓰고 있다", 
    "상상하고 있다", "미소짓고 있다", "가르치고 있다", "놀고 있다"
]

# 동물 행동과 사물 조합 생성
def generate_animal_object_action():
    obj = random.choice(objects)
    animal = random.choice(animals)
    action = random.choice(actions)
    place = random.choice(places)  # 장소 추가
    return f"{animal}는 {place}에서 {obj}를 {action}."

# 해시태그 생성 함수 (장소 추가)
def hashtags_generator(animal, obj, place):
    hashtags = [
        f"#{animal}", f"#{obj}", f"#{animal}_{obj}", f"#{obj}_with_{animal}", 
        f"#{place}",  # 장소 해시태그 추가
        f"#animals", f"#dallE", 
        f"#aiart", f"#openai", f"#chatgpt", f"#automation"
    ]
    print(hashtags)
    return " ".join(hashtags)

# 캡션 생성 (장소 반영)
def caption_generator(action_sentence):
    animal = action_sentence.split("는")[0]  # 동물 추출
    obj = action_sentence.split("를")[0].split("는")[1].strip()  # 사물 추출
    place = action_sentence.split("에서")[0].split("는")[1].strip()  # 장소 추출
    hashtags = hashtags_generator(animal, obj, place)  # 장소 포함된 해시태그 생성

    caption = f"""This post was totally automated using 'dall-e-3'.
---------------------------------------------
{hashtags}
"""
    return caption

import re  # 정규 표현식 모듈

def save_image_to_desktop(image_url, action_sentence):
    # 저장할 경로
    save_directory = r"C:\Users\User\Desktop\이미지생성"
    
    # 경로가 존재하지 않으면 생성
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # 안전한 파일 이름 생성 (사용할 수 없는 문자 제거)
    safe_action_sentence = re.sub(r'[<>:"/\\|?*]', '', action_sentence)  # 파일 이름에 사용 불가 문자 제거
    file_name = f"{safe_action_sentence.replace(' ', '_')}.png"  # 공백을 언더스코어로 대체
    file_path = os.path.join(save_directory, file_name)

    # 이미지 다운로드
    response = requests.get(image_url)
    if response.status_code == 200:
        try:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"이미지가 저장되었습니다: {file_path}")
        except Exception as e:
            print("파일 저장 중 오류 발생:", e)
    else:
        print("이미지 다운로드 실패:", response.status_code)


# 메인 함수
def main():
    action_sentence = generate_animal_object_action()
    print(action_sentence)
    prompt = use_chatGPT(action_sentence)
    print(prompt)

    image_url = use_dallE(prompt)
    caption = caption_generator(action_sentence)
    save_image_to_desktop(image_url, action_sentence)
    postImage(image_url, caption)

if __name__ == "__main__":
    main()
