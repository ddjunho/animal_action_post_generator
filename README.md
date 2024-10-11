# 자동 이미지 게시기 (Automated Image Poster)

이 프로젝트는 OpenAI의 DALL-E와 Instagram API를 사용하여 자동으로 이미지를 생성하고 Instagram에 게시하는 스크립트입니다. 이 스크립트는 랜덤으로 선택된 동물, 사물, 행동, 장소를 조합하여 캡션을 생성하고, 생성된 이미지를 저장한 후 Instagram에 게시합니다.

## 목차
- [기능](#기능)
- [설치](#설치)
- [사용법](#사용법)
- [환경 변수 설정](#환경-변수-설정)
- [기여](#기여)
- [면책 조항](#면책-조항)

## 기능
- OpenAI의 GPT-4 모델을 사용하여 이미지 생성에 대한 프롬프트 생성
- DALL-E API를 사용하여 이미지를 생성
- Instagram API를 사용하여 이미지를 게시
- 게시할 이미지와 캡션에 대한 해시태그 자동 생성
- 이미지 파일을 로컬 디스크에 저장
![Example Image](https://github.com/ddjunho/animal_action_post_generator/blob/main/%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%83%9D%EC%84%B1/%EB%8B%A4%EB%9E%8C%EC%A5%90%EB%8A%94_%ED%8C%90%ED%83%80%EC%A7%80_%EC%88%B2%EC%97%90%EC%84%9C_%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A5%BC_%EC%95%89%EC%95%84_%EC%9E%88%EB%8B%A4..png)
## 설치
1. Python 3.7 이상 설치
2. 필요 라이브러리 설치:
   ```bash
   pip install requests openai
   ```
3. Facebook과 Instagram API에 대한 인증 정보를 `creds.py` 파일에 추가:
  ㄴ

## 사용법
1. 스크립트를 실행합니다:
   ```bash
   python animal_action_post_generator.py
   ```
   이 스크립트는 자동으로 이미지를 생성하고 Instagram에 게시합니다.

## 환경 변수 설정
스크립트를 실행하기 전에 `creds.py` 파일을 설정하여 필요한 API 키와 기타 정보를 포함해야 합니다. 모든 정보는 [Facebook 개발자 문서](https://developers.facebook.com/docs/)와 [OpenAI API 문서](https://platform.openai.com/docs/)에서 확인할 수 있습니다.


## 기여
기여를 원하시면, 이 리포지토리를 포크하고 변경 사항을 풀 리퀘스트로 제출해주세요.

## 면책 조항
이 프로젝트는 교육 및 실험 목적으로만 제공됩니다. 실제로 API를 사용하여 콘텐츠를 게시할 때는 Facebook 및 Instagram의 정책을 준수해야 합니다.
