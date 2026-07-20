# 使用ImageBreed管理田間影像與育種計劃
完成ImageBreed安裝後即可進入進入管理頁面，管理育種計劃。須先登入管理員帳號，預設管理員帳號密碼如下
```
帳號：admin
密碼：password
```
## 1. 管理組織
進入[http://localhost:70/breeders/companies/](http://localhost:70/breeders/companies/)管理組織

### 1.1 新增組織
點選新增組織按鈕，依照指示將資訊填入組織資訊，點選繼續，若有成功加入將會顯示建立完成，點選關閉即可。

## 2. 管理育種計劃
進入[http://localhost:70/breeders/manage_programs/](http://localhost:70/breeders/manage_programs)管理育種計劃

### 2.1 新增育種計劃
點選新增育種計劃按鈕，依照指示將資訊填入育種計劃資訊，點選儲存育種計劃，若有成功加入將會顯示建立完成，點選關閉即可。

## 3. 管理田區位置
進入[http://localhost:70/breeders/locations](http://localhost:70/breeders/locations)管理田區位置

### 3.1 新增田區    
在下方地圖點選田區位置，於彈出視窗點選新增田區，填寫田區資訊，點選儲存田區，若有成功加入將會顯示建立完成，點選關閉即可。

## 4. 管理品系資料
進入[http://localhost:70/breeders/accessions/](http://localhost:700/breeders/accessions/)管理品系，點選新增品系或上傳品系資訊，選擇唱傳檔案獲得品系清單範本。

### 4.1 製作品系清單
製作品系清單的 Excel 檔 (.xls or .xlsx)，依據範本填入`accession_name`	品系資訊與`species_name`物種名稱，其他項目可選擇性填入

### 4.2 上傳品系清單
回到網站頁面，將製作完成的品系清單上傳至網站，點選繼續，若有成功加入將會顯示建立完成，點選建立完成，點選關閉即可。

## 5. 管理試驗資料
進入[http://localhost:70/breeders/trials/](http://localhost:70/breeders/trials/)管理試驗資料，點選試驗所在組織，顯則上傳試驗資料或建立試驗，依據網站引導建立試驗

## 6. 管理影像拍攝無人機
進入[http://localhost:70/breeders/drone_rover](http://localhost:70/breeders/drone_rover)管理影像拍攝無人機

## 7. 管理影像資料
進入[http://localhost:70/breeders/images/](http://localhost:70/breeders/images/)管理影像資料

目前僅支援上傳正射後影像，空拍後影像須先透過正射軟體如Pix4D等完成影像正射與拼接後上傳至系統

### 7.1 上傳正射影像
點選上傳影像，選擇先前建立完成所屬組織與試驗，輸入影像拍攝日期與時間，選取拍攝細節如影像解析度、影像感測測器類型、拍攝無人機與電池以及此次拍攝的描述，後續再將影像上傳至對應波段，即完成影像上傳

### 7.2 影像處理
依據畫面指示旋轉使田區四周與邊界平行，剪裁出田間區域
