

'''
1. 'MIN' 기법 구현
'''

def MIN(reference_list, frame_n):
    memory = []  
    page_fault = 0  

    print("초기 메모리 상태 : ", memory)

    for idx, page in enumerate(reference_list) :    
        print("")
        print(f"time = {idx + 1} :  {page} 페이지 참조")                  # 페이지 참조 리스트 중 각 페이지에 대해서

        if page not in memory :                                       # 메모리에 페이지가 없다면 Page Fault 발생
            print(" !! page fault 발생 !! ")
            page_fault += 1                                           
            if len(memory) < frame_n :                                  # 1. 메모리가 차 있지 않다면 메모리에 페이지 추가
                memory.append(page)
            else :                                                      # 2. 메모리가 차 있다면
                forward_distances = []
                forward_references = reference_list[idx+1:]
                for in_page in memory :                                                 # 1) 메모리에 이미 있는 페이지에 대해서 각각 forward distance 구하기
                    try :
                        forward_distances.append(forward_references.index(in_page))     # 1-1) 미래 참조 리스트의 인덱스를 저장한다.
                    except :
                        forward_distances.append(9999)                                                          # 1-2) 미래 참조 리스트에 없을 경우, 9999을 저장한다. (max 값)
                max_indexs = [idx for idx, x in enumerate(forward_distances) if x == max(forward_distances)]   # 제일 먼 미래에 참조되는 페이지의 메모리 인덱스들의 값 
                if len(max_indexs) == 1 :                                                                       # 2) victim이 하나라면, memory의 victim 자리를 현재 페이지로 교체
                    memory[max_indexs[0]] = page
                else :
                    p_num = [memory[idx] for idx in max_indexs]           # 3) tie-breaking: 큰 것 기준으로 ! victim이 여러개일 경우, 페이지 넘버가 가장 큰 페이지를 찾고, memory에서 그 victim의 위치를 페이지로 교체
                    memory[memory.index(max(p_num))] = page 
                    print("tie-breaking : page number가 큰 것을 기준으로 교체한다.")
        print('현재 memory state : ', memory)
    print("")
    print("=> 총 page fault 개수 : ", page_fault)


'''
2. 'FIFO' 기법 구현
'''


def FIFO(reference_list, frame_n):
    memory = []  
    page_fault = 0  
    load_time_stamping = []  # 처음 로딩될 때 기록

    print("초기 메모리 상태 : ", memory)
    for idx, page in enumerate(reference_list) : 
        print("")
        print(f"time = {idx + 1} :  {page} 페이지 참조")                  # 페이지 참조 리스트 중 각 페이지에 대해서

        if page not in memory :                                       # 메모리에 페이지가 없다면 Page Fault 발생
            print(" !! page fault 발생 !! ")
            page_fault += 1                                           
            load_time_stamping.append(page)                           # 메모리 첫 로딩 시점에 기록 (순서대로 기록된다)

            if len(memory) < frame_n :                                  # 1. 메모리가 차 있지 않다면 메모리에 페이지 추가
                memory.append(page)
            else :                                                      # 2. 메모리가 차 있다면
                old_page = load_time_stamping.pop(0)     # 1) load time 리스트에 가장 먼저 들어온 페이지를 찾고, load time 리스트에서 삭제
                memory[memory.index(old_page)] = page   # 2) 메모리에서 해당 위치를 교체
        print('현재 memory state : ', memory)
    print("")
    print("=> 총 page fault 개수 : ", page_fault)



'''
3. 'LRU' 기법 구현
'''

def LRU(reference_list, frame_n):
    memory = []  
    page_fault = 0  
    reference_time_stamping = []  # 가장 최근 참조될 때 기록

    print("초기 메모리 상태 : ", memory)
    for idx, page in enumerate(reference_list) : 
        print("")
        print(f"time = {idx + 1} :  {page} 페이지 참조")                  # 페이지 참조 리스트 중 각 페이지에 대해서

        if page in reference_time_stamping :                            # 기존에 참조된 것이라면, 해당 내역 삭제 해 재참조 반영
            reference_time_stamping.remove(page)
        reference_time_stamping.append(page)

        if page not in memory :                                       # 메모리에 페이지가 없다면 Page Fault 발생
            print(" !! page fault 발생 !! ")
            page_fault += 1                                           

            if len(memory) < frame_n :                                  # 1. 메모리가 차 있지 않다면 메모리에 페이지 추가
                memory.append(page)
            else :                                                      # 2. 메모리가 차 있다면
                old_page = reference_time_stamping.pop(0)     # 1) 참조 리스트 중 가장 오래전에 참조된 페이지를 찾고, 리스트에서 삭제
                memory[memory.index(old_page)] = page   # 2) 메모리에서 해당 위치를 교체
        print('현재 memory state : ', memory)
    print("")
    print("=> 총 page fault 개수 : ", page_fault)


'''
4. 'LFU' 기법 구현
'''


def LFU(page_n, reference_list, frame_n):
    memory = []  
    page_fault = 0  
    reference_counting = [0]*(page_n+1)  # counting 횟수 기록
    reference_time_stamping = []  # Tiebreaking 위해 LRU : 가장 최근 참조될 때 기록

    print("초기 메모리 상태 : ", memory)
    for idx, page in enumerate(reference_list) : 
        print("")
        print(f"time = {idx + 1} :  {page} 페이지 참조")                  # 페이지 참조 리스트 중 각 페이지에 대해서

        reference_counting[page] += 1                                 # 페이지 참조 횟수 증가

        if page in reference_time_stamping :                            # Tiebreaking 위해 LRU : 기존에 참조된 것이라면, 해당 내역 삭제 해 재참조 반영
            reference_time_stamping.remove(page)
        reference_time_stamping.append(page)

        if page not in memory :                                       # 메모리에 페이지가 없다면 Page Fault 발생
            print(" !! page fault 발생 !! ")
            page_fault += 1                                           

            if len(memory) < frame_n :                                  # 1. 메모리가 차 있지 않다면 메모리에 페이지 추가
                memory.append(page)
            else :                                                      # 2. 메모리가 차 있다면
                compare_list = [reference_counting[page] for page in memory] # 해당 reference counting 비교
                min_count = min(compare_list)                               # 가장 작은 값
                if compare_list.count(min_count) == 1 :                     # 1) 가장 작은 값이 1개면
                    memory[compare_list.index(min_count)] = page            # 메모리에서 해당 위치 교체
                else :                                                      # 2) 가장 작은 값이 여러개면 tie-breaking : LRU
                    for p in reference_time_stamping :
                        if reference_counting[p] != min_count :
                            reference_time_stamping.remove(p)
                    old_page = reference_time_stamping.pop(0)     # 1) 참조 리스트 중 가장 오래전에 참조된 페이지를 찾고, 리스트에서 삭제
                    memory[memory.index(old_page)] = page   # 2) 메모리에서 해당 위치를 교체

        print('현재 memory state : ', memory)
    print("")
    print("=> 총 page fault 개수 : ", page_fault)




'''
5. 'WS' 기법 구현
'''


def WS(page_n, reference_list, window_size):
    memory = []  
    page_fault = 0  
    working_set = []
    
    print("초기 메모리 상태 : ", memory)
    for idx, page in enumerate(reference_list) : 
        print("")
        print(f"time = {idx + 1} :  {page} 페이지 참조")                  # 페이지 참조 리스트 중 각 페이지에 대해서

        working_set.append(page)

        if page not in memory :                                       # 메모리에 페이지가 없다면 Page Fault 발생 & 추가
            print(" !! page fault 발생 !! ")
            page_fault += 1                                           
            memory.append(page)  
            memory.sort()                        
            print("Pws = ", page)
            
        if len(working_set) > window_size + 1 :                       # W(t, window_size) 만큼의 참조된 리스트 유지 위해
            old_page = working_set.pop(0)                             # 가장 예전에 참조된 페이지 poop
            if old_page not in working_set :                          # 만약 최근에 참조되지 않았다면 memory에서 remove
                memory.remove(old_page)
                print("Qws = ", old_page)
        
        print('현재 memory state : ', memory)

    print("")
    print("=> 총 page fault 개수 : ", page_fault)



'''
input.txt 파일 읽고, 입력값 저장
'''

try : 
    input_file = open('./input.txt', 'r')
    input_txt = input_file.readlines()
except :
    print('읽어들이지 못하였습니다.')
finally :
    input_file.close()


variable_list = list(map(int, input_txt[0].strip().split()))
page_n, frame_n, window_size, reference_len = variable_list
reference_list = list(map(int, input_txt[1].strip().split()))

'''
결과 출력
'''

print("------------------------------- MIN 기법 -------------------------------")
print("")
MIN(reference_list, frame_n)
print("")

print("------------------------------- fifo 기법 -------------------------------")
print("")
FIFO(reference_list, frame_n)
print("")

print("------------------------------- LRU 기법 -------------------------------")
print("")
LRU(reference_list, frame_n)
print("")

print("------------------------------- LFU 기법 -------------------------------")
print("")
LFU(page_n, reference_list, frame_n)
print("")

print("------------------------------- WS 기법 -------------------------------")
print("")
WS(page_n, reference_list, window_size)
print("")