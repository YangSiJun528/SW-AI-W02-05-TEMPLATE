# Skill: Import Weekly Issues

## Description
weekN 폴더의 CSV 파일을 읽어 GitHub 이슈를 생성하고 GitHub Project에 추가하는 스킬.

## Trigger
- 사용자가 "weekN 이슈 추가", "weekN 프로젝트에 올려" 등 특정 주차를 명시하며 이슈 생성을 요청할 때
- 반드시 weekN 형태의 인자를 받아야 함 (예: week1, week2, week10 등)
- 주차 정보가 없으면 실행하지 않고, 어떤 주차인지 반드시 확인할 것

## Constraints
- 사용자가 weekN을 명시적으로 입력하거나 말하지 않으면 절대 실행하지 않는다
- 실행 전 반드시 사용자에게 확인을 받는다

## Flow

### 1. 입력 검증
- 사용자가 weekN(예: week2)을 명시했는지 확인
- 명시하지 않았다면: "몇 주차인지 알려주세요 (예: week2)" 라고 물어보고 대기

### 2. CSV 파일 읽기
- `weekN/weekN_issues_complete.csv` 파일을 읽는다
- CSV 형식: `title,content` (첫 행은 헤더)
- content가 있으면 이슈 본문에 포함, 없으면 빈 본문

### 3. 프로젝트 확인
- `gh project list --owner @me --format json`으로 프로젝트 목록 조회
- 프로젝트가 여러 개면 어떤 프로젝트에 추가할지 사용자에게 확인

### 4. 사용자 확인 (필수)
- 생성할 이슈 목록을 요약하여 보여준다:
  - 총 이슈 개수
  - 카테고리별 분류 (공통, basic, 문제풀이, Extra 등)
  - 대상 프로젝트 이름
- "이대로 진행할까요?" 라고 확인을 받는다
- 사용자가 승인해야만 다음 단계로 진행

### 5. 이슈 생성 및 프로젝트 추가
- CSV의 각 행에 대해:
  - `gh issue create --repo <REPO> --title "<title>" --body "<content>"` 로 이슈 생성
  - `gh project item-add <PROJECT_NUM> --owner @me --url <issue_url>` 로 프로젝트에 추가
- 모든 이슈 생성 완료 후 결과 요약 출력

### 6. 결과 보고
- 생성된 이슈 개수
- 프로젝트에 추가된 아이템 수
- 오류가 있었다면 해당 내용 보고
