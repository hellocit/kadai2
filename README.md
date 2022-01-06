# kadai2

# myled
2021年度ロボットシステム学の課題2で
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/20




三つのプログラムを参考にして作成したデバイスドライバです。

# 動作環境
Raspberry Pi 4 Model B

OS : ubuntu 20.04 server

使用したもの


・Raspberry Pi 4 Model B × 1

・モータ用電源　1.5V使用済み単三電池 × 3

・ＴＢ６７Ｈ４５０モータドライバモジュール× 1

・ブレッドボード × 1

・ジャンパー線（オス-メス）× 5

・ジャンパー線（オス-オス）× 1

・サンハヤト製ブレッドボード用ジャンプワイヤ × 2

# 回路図
![robosis](https://user-images.githubusercontent.com/91714744/145830010-5c700ab9-eeb2-4f1c-ba59-2d3dc1206ba5.png)
# プログラムの実行方法
## ［インストール］
```
git clone git@github.com:hellocit/myled.git

cd myled

make

sudo insmod myled.ko

sudo chmod 666 /dev/myled0
```
## ［アンインストール］

```
sudo rmmod myled

make clean
```

## ［実行］
## LEDを点灯するコマンド
```
echo 1 > /dev/myled0
```
## LEDを消灯するコマンド
```
echo 0 > /dev/myled0
```

# 結果
https://www.youtube.com/watch?v=qx7kacyVDzc
# ライセンス
https://github.com/hellocit/myled/blob/main/COPYING
# 作成するにあたり引用したプログラム
https://github.com/ryuichiueda/robosys_device_drivers/blob/master/myled10.c
