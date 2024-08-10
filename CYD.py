'我的主页'
'我的主页'
import streamlit as st
import time
from PIL import Image
import pandas as pd
page = st.sidebar.radio('我的首页',['飞友狂欢主页','飞友的图片处理工具','空中浩劫全集超链接','飞友的英文词典','飞友留言区','飞马游戏推荐','实时新闻'])
def page1():
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.download_button(label = '下载歌曲',data = mymp3, file_name = 'Counting Stars.mp3')
    st.image('86.png')
    st.image('87.png')
    st.image('88.png')
    msg = ':blue[飞友大狂欢]'
    msg2 = ':blue[播放网页最上方的音乐，看看这些图片。]'
    st.write(msg)
    st.write(msg2)
    st.image('81.png')
    st.image('82.png')
    st.image('83.png')
    st.image('84.png')
    st.image('85.png')
    d = {'波音': ['707', '717', '727', '737', '747', '757', '767', '777', '787'], '空客': ['A220', 'A310', 'A319', 'A320', 'A321', 'A330', 'A340', 'A350', 'A380']}
    a = pd.DataFrame(d)
    st.write(a)
def page2():
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    msg3 = ':blue[:sunglasses:飞友的图片处理工具（可以将处理的图片发到留言区哦）:sunglasses:]'
    st.write(msg3)
    uploaded_file = st.file_uploader('上传图片',type = ['png' ,'jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        t1,t2,t3,t4 = st.tabs(['原图','改色1','改色2','改色3'])
        with t1:
            st.image(img)
        with t2:
            st.image(img_change(img, 0, 2, 1))
        with t3:
            st.image(img_change(img, 1, 0, 2))
        with t4:
            st.image(img_change(img, 2, 1, 0))



def page3():
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    st.link_button('1~14季空中浩劫', 'https://www.bilibili.com/video/av12168252/')
    st.link_button('15季空中浩劫', 'https://www.bilibili.com/video/av499463045/')
    st.link_button('16季空中浩劫', 'https://www.bilibili.com/video/BV1xD4y1m7mw/')
    st.link_button('17季空中浩劫', 'https://www.bilibili.com/video/BV11T4y1w7sw?p=3')
    st.link_button('18季空中浩劫', 'https://www.bilibili.com/video/av46907972/')
    st.link_button('19季空中浩劫', 'https://www.bilibili.com/video/av711878797/')
    st.link_button('20季空中浩劫', 'https://www.bilibili.com/video/av711958221/')
    st.link_button('21季空中浩劫', 'https://www.bilibili.com/read/cv12356007/')
    st.link_button('22季空中浩劫', 'https://www.bilibili.com/read/cv16012570/')
def page4():
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    st.write(':blue[:sunglasses:飞友的英文词典:sunglasses:]')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])



def page5():
    global name
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    st.write(':sunglasses:飞友留言区:sunglasses:')
    st.write('对不起飞友们，这个聊天框是很老的版本了，所以有一些小bug。你必须按两次留言键（虽然会显示两次，不过不影响，按一次显示不了）：')
    name = st.text_input('你想在网站中用的名字是：')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '张三':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == '李四':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == name:
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def page6():
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    msg4 = ':blue[:sunglasses:TFS:sunglasses:]'
    msg5 = ':blue[:sunglasses:RFS:sunglasses:]'
    msg6 = ':blue[:sunglasses:GeoFS:sunglasses:]'
    msg7 = ':blue[:sunglasses:AeroflyFSGlobal:sunglasses:]'
    msg8 = ':blue[:sunglasses:Xplane:sunglasses:]'
    msg9 = ':blue[:sunglasses:infiniteFlight:sunglasses:]'
    st.write(msg4)
    st.write(msg5)
    st.write(msg6)
    st.write(msg7)
    st.write(msg8)
    st.write(msg9)
def page7():
    with open('1.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time = 0)
    st.title('沉痛')
    st.header(':cry:巴西沃帕斯航空2283号班机在当地时间8月9日在巴西东南部圣保罗州维涅杜市坠毁，机上61人全部遇难:cry:')

def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x, y] = (r, g, b)
    return img


if (page == '飞友狂欢主页'):
    page1()
elif (page == '飞友的图片处理工具') :
    page2()
elif (page == '空中浩劫全集超链接') :
    page3()
elif (page == '飞友的英文词典') :
    page4()
elif (page == '飞友留言区') :
    page5()
elif (page == '飞马游戏推荐') :
    page6()
elif (page == '实时新闻') :
    page7()