import glob, os

##############################################

# 目標資料夾的名稱 ( 放到 ./data 當中 )
trg_dir = '放圖片的資料夾名稱'

# 宣告多少筆數據要變成測試資料
percentage_test = 30

##############################################


# 確保資料集存在
datasets_path = f'data/{trg_dir}'

if os.path.exists(datasets_path):
  
  # 取得 train.txt , test_txt 的完整路徑
  train_txt_path = f'data/{trg_dir}_train.txt'
  test_txt_path = f'data/{trg_dir}_test.txt'

  # 確認是否移動到當前目錄
  os.chdir('/content/drive/MyDrive/yolov4/darknet')
  print('當前路徑為:', os.getcwd())

  # 宣告資料集路徑
  dataset_dir = f'data/{trg_dir}'
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

else:

  print(f'Check the target datasets is exists ({datasets_path})')