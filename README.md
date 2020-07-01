# mmsensor_co2
三密予防センサー　CO2計測センサー


# 概要
  
 三密要望システムのCO2計測カメラプログラムです。
    
 CO2センサー(MH_Z19)を装着したRaspberryPi側で動作し、検知されたCO2濃度を指定のURLに投稿します。

# 導入方法
  
RaspberryPi上で以下を実行します。
  
# ソースのチェックアウト
```
git clone https://github.com/tt-hasegawa/mmsensor_co2.git
```

# 依存ライブラリのインストール
```
cd mmsensor_co2
pip3 install -r ./requirements.txt
```


# URLの編集
  
 CO2Sensor.pyの冒頭以下の部分を環境に即した値に変更する。

``` 
url='http://192.168.46.128:3000' # 接続先herokuサーバのURL
proxies = { # Proxyがある場合
    'http': 'http://proxy:12080',
    'https': 'http://proxy:12080'
}
proxies = { # Proxyが無い場合
   'http': None,
   'https': None
}
```

# 実行登録
  
 以下のコマンドを実行し、cronに登録があるか、確認する。
```
crontab -l
``` 
 有無を確認する行
```
@reboot /bin/sh /home/pi/mmsensor_co2/co2-sensor.sh
```
 登録が無ければ、以下のコマンドでcronの編集モードに入り、追記する。
```
crontab -e
```
末尾に以下を追記する。
```
@reboot /bin/sh /home/pi/mmsensor_co2/co2-sensor.sh
```

# 再起動する。
```
sudo reboot
```
# ログ確認
 以下のコマンドで実行ログを確認する。

```
tail -f /tmp/sensor-co2.log
```
 ログ確認を止める場合、Ctrl + C
