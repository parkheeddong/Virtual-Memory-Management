# Virtual-Memory-Management
Demand paging system을 위한 page replacement 기법 구현 및 검증

<br />

### ✨ 프로젝트 내용
#### 주어진 page reference string을 입력 받아, 
#### replacement 기법으로 처리했을 경우의 memory residence set 변화 과정 및 page fault 발생 과정 추적/출력

<br />


### ✅ 구현한 기법
#### MIN, FIFO, LRU, LFU, WS Memory Management

* Min 기법 Tie Breaking Rule : 페이지 넘버가 큰 페이지 교체
* LFU 기법 Tie Breaking Rule : LRU 기법


<br />

  
### ✅ 가정
Page frame 할당량 및 window size 등은 입력으로 결정

<br />

  
### ✅ 입력 포맷
N M W K
r1 r2 r3 r4 r5 ∙∙∙ rK

### Example
`6 3 3 15`
<br />
`0 1 2 3 2 3 4 5 4 1 3 4 3 4 5`
<br />
N은 process가 갖는 page 개수 (최대 100)
M은 할당 page frame 개수 (최대 20, WS 기법에서는 비사용)
W는 window size (최대 100, WS 기법에서만 사용)
K는 page reference string 길이 (최대 1,000)


<br />

  
#### 개발 환경 WindowS
#### 개발 플랫폼 VSCODE
#### 언어 Python

<br />

  
