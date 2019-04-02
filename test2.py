# coding:utf-8
import urllib.request
import re


def get_html(url):
    page = urllib.request.urlopen(url)
    html_code = page.read()
    return html_code


def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        urllib.request.urlretrieve(img, 'd:/py_img/%s.jpg' % x)
        x += 1


print('-------网页图片抓取-------')
print('请输入url:'),
url = input()
if url:
    pass
else:
    print('---没有地址输入正在使用默认地址---')
    url = 'http://tieba.baidu.com/p/1753935195'
print('----------正在获取网页---------')
html_code = get_html(url)
print('----------正在下载图片---------')
get_image(html_code.decode('utf-8'))
print('-----------下载成功-----------')
input('Press Enter to exit')
