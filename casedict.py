class Bunch(dict):
    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        pass
    

#--- issue list ---
'''
issue 編號請和evernote的issue tracking一致
[Trial Run] 5L AI Issue Summary
https://www.evernote.com/shard/s223/sh/00deb2de-8f67-4dc4-a62b-38db580a5a8d/ec341e1c3f66c5ab13526402ec16f816
'''

issue_10 = Bunch(
    vpath='/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-06 78.26 R11.12_20201013210000-20201013211000_1.mp4',
    desc = '工作檯上有粉紅色PPEN2',
    video_len = None,
    )

issue_13 = Bunch(
    vpath= '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-07 78.31 R11.12_202010292220.mp4',
    desc = '沒有bbox',
    video_len = None,
    )

issue_14 = Bunch(
    vpath= '',
    desc = 'Flash亮度逐漸變大',
    video_len = None,
    )

issue_15 = Bunch(
    vpath= '',
    desc = '誤判料盒為BBOX',
    video_len = None,
    )

issue_16 = Bunch(
    vpath= '',
    desc = '工具顏色亮度較暗',
    video_len = None,
    )

issue_17 = Bunch(
    vpath='/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-01 78.69 R11.12_20201017093200-20201017093700_1.mp4',
    desc = '手腕處的黃色手套誤偵測為為TZS',
    video_len = None,
    )

issue_18 = Bunch(
    vpath= '',
    desc = '工具被手遮擋, 無法用顏色辨識',
    video_len = None,
    )

issue_19 = Bunch(
    vpath='',
    desc = '頭套誤判為閃光',
    video_len = None,
    )

issue_dict = {
    'issue_10': issue_10,
    'issue_13': issue_13,
    'issue_14': issue_14,    
    'issue_15': issue_15,
    'issue_16': issue_16,
    'issue_17': issue_17,    
    'issue_18': issue_18,    
    'issue_19': issue_19
}

def get_issue_list(echo=True):
    if echo:
        print('\n---- issue list ---\n')
        for k in issue_dict.keys():
            print(f'{k}:', issue_dict.get(k).desc)
    return issue_dict


#------
'''
目前沒有建立demo case lise. 暫時根據PM需求定義case
'''

demo_1 = Bunch(
    vpath='/mnt/hdd1/ipcamera_case_data/output/N01-3F 05L F68-02 78.42 R11.12_202010290833.mp4',
    desc = '跳過工序5',
    video_len = None,
    )

demo_case_dict={
    'demo_1':demo_1,
}    



