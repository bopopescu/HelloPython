import tkinter
import tkinter.messagebox


def main():
    flag=True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg= ('red','Hello world')\
            if flag else ('blue','Goodbye')
        label.config(text=msg,fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('?','quit????'):
            top.quit()

    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('Hahahaha')
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()