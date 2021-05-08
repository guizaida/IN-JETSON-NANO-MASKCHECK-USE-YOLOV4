import glob 
import os

##############################################


# 宣告多少筆數據要變成測試資料
percentage_test = 10;

##############################################




  
# 取得 train.txt , test_txt 的完整路徑
train_txt_path = r"C:\Users\guizaida\Desktop\111\train.txt"
test_txt_path = r'C:\Users\guizaida\Desktop\111\test.txt'


# 宣告資料集路徑
dataset_dir = 'C:\\Users\guizaida\Desktop\maskcheck'
print('目標資料夾:', dataset_dir)

# 建立以及開啟 train.txt, test.txt
file_train = open(train_txt_path, 'w')
file_test = open(test_txt_path, 'w')

# 開始輸入訓練資料
counter = 1
index_test = round(100 / percentage_test)

# glob.iglob 可以將該目錄下所有的 .jpg 儲存成一個 List
for file_path in glob.iglob(os.path.join(dataset_dir, "*.jpg")):
      
      if counter == index_test:
          counter = 1
          file_test.write(file_path + "\n")
      else:
          file_train.write(file_path + "\n")
          counter = counter + 1

file_train.close()
file_test.close()
print('Finish')

