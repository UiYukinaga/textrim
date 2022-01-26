# textrim
テキストファイルのデータ処理ツール。テキストファイル各行の先頭または末尾の任意文字数削除する。

## 使い方
1. コマンドを実行
```
python3 textrim.py
```
2. 編集したいテキストファイルのフルパスを入力する
```
Input a TEXT file path: C:/users/***/***/hoge.txt
```

4. モードを選択(入力)する
```
Select a mode[h:Head trim, t:Tail trim, q: Quit]: h
```
　　'h'：先頭文字トリムモード（先頭から指定文字数削除したい場合）
    't'：末尾文字トリムモード（末尾から指定文字数削除したい場合）

4. 削除する文字数を入力する
```
Input a number of trimming: 3
```
　　任意の削除したい文字数を入力する
