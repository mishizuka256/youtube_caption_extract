# -*- coding: utf-8 -*-
import os
from pytube import YouTube
import xml.etree.ElementTree as ET
import codecs


def outContext(url):
    #動画のクラス取得
    yt = YouTube(url)
    # 動画の字幕の言語一覧
    print(yt.captions.get_by_language_code)
    # 指定した言語の字幕取得
    # caption = yt.captions.get_by_language_code('a.ja')
    caption = yt.captions.get_by_language_code('a.en')

    import pdb; pdb.set_trace()
    # srt形式で取得
    
    # contexts = caption.generate_srt_captions()  
    contexts = caption.xml_captions
    # ファイルに出力
    f = open(yt.video_id + '.srt', 'w')
    f.write(contexts)
    f.close()

    path = yt.video_id + '.srt'

    tree = ET.parse(path)
    root = tree.getroot()
    notags = ET.tostring(root, method='text')
    notags = notags.decode('utf8')

    lst = notags.split('\n')
    lst_contents = []
    for content in lst:
        if content != '':
            lst_contents.append(content)
    print(lst_contents)

    with open(yt.video_id + '.txt', 'w')as fw:
        fw.write('\n'.join(lst_contents))

common_url = "https://www.youtube.com/watch?v=iIhJ_IJvyPY"
outContext(common_url)
