# kadai2
2021年度ロボットシステム学の課題2で  
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/20  
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/22  
上記二つのプログラムを引用かつ改変し作成しました。
実行すると3の倍数だけがcount.pyで表示されます。
少し待つと世界が平和になるものが表示されるかも...

# 動作環境
・Raspberry Pi 4 Model B

・OS : ubuntu 20.04 server


# プログラムの実行方法
## ［インストール］
```
$ git clone git@github.com:hellocit/kadai2.git

$ cd ~/kadai2/scripts/

$ chmod +x count.py

$ chmod +x sub.py
```
## ［実行］
事前に二つの端末を開きます。rosrunの順番は端末1→端末2です。
***
端末1
```
$ roscore &
$ rosrun kadai2 sub.py
```

端末2
```
$ rosrun kadai2 count.py
```


# 結果

# ライセンス
https://github.com/hellocit/kadai2/blob/main/LICENSE
# 改変し、作成するにあたり引用したプログラム
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/20  
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/22
# 参考
用語を調べたサイト  
https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/appendix/ros_word  
Pythonを調べたサイト  
https://www.sejuku.net/blog/21909  
https://www.delftstack.com/ja/howto/python/python-print-string-and-variable/  
ヒント  
http://www.edu.i.hosei.ac.jp/~sigesada/kyouzai/mojicodehenkan.html  




