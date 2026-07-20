# ImageBreed 安裝
ImageBreed 是一個基於 Docker 的應用程式，您可以使用以下步驟來安裝它

## 0. 安裝前準備
### 0.1 安裝 Docker
請先安裝 Docker，您可以參考官方文件來安裝 Docker：
- [Docker 官方文件](https://docs.docker.com/get-docker/)    
### 0.2 安裝 Docker Compose
請先安裝 Docker Compose，您可以參考官方文件來安裝 Docker Compose：
- [Docker Compose 官方文件](https://docs.docker.com/compose/install/)   
### 0.3 安裝 Git
請先安裝 Git，您可以參考官方文件來安裝 Git：
- [Git 官方文件](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)   
### 0.4 申請API Key (非必要)
若需要利用氣後相關服務，請先申請中央氣象署 OpenData API 或農業部農業氣象 API Token，您可以參考官方文件來申請 API Key：
- [中央氣象署 OpenData API](https://opendata.cwa.gov.tw/userLogin)
- [農業氣象 API Token 申請](https://weather.moa.gov.tw/apply/edit)

## 1. ImageBreed
本頁面提供中文版本ImageBreed指引，按照接續步驟完成安裝
### 1.1 安裝 ImageBreed
利用git下載本頁面並進入完成後的資料夾，在欲安裝的位置輸入`cmd`打開終端機，並在終端機輸入下方指令並執行：
```bash
git clone https://github.com/74207281/imagebreed_dockerfile_zh.git
```
### 1.2 填入API
將步驟 0.4 申請的 API Token 填入控制檔，使系統可獲得API Token獲取氣象資料。

打開`development`資料夾內的`sgn_local_docker.conf`，在第55行`cwa_token`後填入獲取的API Token，如下：
```
cwa_token YOUR_TOKEN
```
將 `YOUR_TOKEN` 改寫為申請好的API Token。

### 1.3 啟動 ImageBreed
利用 docker compose 啟動 ImageBreed，在終端機輸入下方指令並執行：
```bash
docker-compose up -d
```
即完成ImageBreed安裝，打開瀏覽器進入[http://localhost:70/](http://localhost:70/)即可進入頁面

若需了解如何使用ImageBreed管理育種計劃與影像資料，請參閱這裏的[使用說明](https://github.com/74207281/imagebreed_dockerfile_zh/blob/main/docs/application.md)


