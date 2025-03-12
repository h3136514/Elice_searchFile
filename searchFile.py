import os
import shutil
import time


# 초기 설정파일에서 정보 추출
data = []
with open("init.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()
f.close()

search_string = data[2][data[2].find('=')+2:] #검색단어
src_path = data[3][data[3].find('=')+2:] # 기존 폴더 경로
new_path = data[4][data[4].find('=')+2:] # 옮길 폴더 경로


# 폴더 안에 있는 모든 하위 파일(서브폴더의 파일 포함)을 읽어 리스트로 반환하는 함수
def read_all_file(path):
    output = os.listdir(path)
    file_list = []

    for i in output:
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)

    return file_list

def copy_all_file(file_list, new_path):
    for src_path in file_list:
        file = src_path.split("/")[-1]
      
        if os.path.basename(file).find(search_string) != -1: # 파일명에 검색단어가 포함되어 있는지
            shutil.copyfile(src_path, new_path+"/"+file)
            print("파일 {} 작업 완료".format(file)) # 작업한 파일명 출력
        
        
start_time = time.time() # 작업 시작 시간 

file_list = read_all_file(src_path)
copy_all_file(file_list, new_path)

print("=" * 40)
print("러닝 타임 : {}".format(time.time() - start_time)) # 총 소요시간 계산

input("끝낼려면 Enter를 두번 입력하세요")
