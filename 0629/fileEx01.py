# newfile.py
# open -> use -> close
f = open("새파일.txt", 'w')
f.close()

# newfile2.py
f = open("C:/doit/새파일.txt", 'w') # 경로 속에 doit 폴더가 없으면 오류 발생
f.close()

# 폴더 만드는 코드
import os

os.makedirs("C:/doit", exist_ok=True)

f = open("C:/doit/새파일.txt", "w")
f.close()

