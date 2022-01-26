import os

def textrim():
    f_path = input('Input a TEXT file path: ')

    f = open(f_path, 'r')
    datalist = f.readlines()
    f.close()

    # 入力されたパスからファイル名を取得する
    f_name = os.path.basename(f_path)
    # 結果ファイルのファイル名を生成する
    new_f_name = 'trimed_' + f_name
    # ディレクトリパスを取得する
    dir_path = os.path.dirname(f_path)
    #処理を実行した結果ファイルのフルパスを生成する
    new_path = os.path.join(dir_path, new_f_name)

    # 処理モードのユーザ選択処理
    loop_en = 1
    while loop_en == 1:
        loop_en = 0
        mode = input('Select a mode[h:Head trim, t:Tail trim, q: Quit]: ')
        if mode == 'h':
            print('HEAD Trim mode')
        elif mode == 't':
            print('TAIL Trim mode')
        elif mode == 'q':
            print('This function was canceled.')
            return 0
        else:
            print('The command you entered is invalid.')
            print('Please try again.')
            loop_en = 1
    
    # トリムする文字数のユーザ入力処理
    loop_en = 1
    while loop_en == 1:
        loop_en = 0
        n_char = input('Input a number of trimming: ')

        if n_char.isdecimal():
            n_trim = int(n_char)
            write_data = []
            for line_str in datalist:
                if mode == 'h':
                    trimed_line = line_str[n_trim:]
                elif mode == 't':
                    trimed_line = line_str[:n_trim]
                
                write_data.append(trimed_line)

        else:
            print('The command you entered is invalid.')
            loop_en = 1

    nf = open(new_path, 'w')
    nf.writelines(write_data)
    nf.close()

    print('Completed!')
    print('Save as', new_path)

    return 0

if __name__ == '__main__':
    textrim()
