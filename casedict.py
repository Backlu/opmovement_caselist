import os 

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
    desc = '工作檯上有粉紅色PPEN2',    
    vpath= '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-06 78.26 R11.12_20201013210000-20201013211000_1.mp4',
    video_len = None,
    )

issue_13 = Bunch(
    desc = '沒有bbox',    
    vpath= '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-07 78.31 R11.12_202010292220.mp4',
    video_len = None,
    )

issue_14 = Bunch(
    desc = 'Flash亮度受現場燈光影響變大變小',    
    vpath= '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-06 78.26 R11.12_20201029212015-20201029222015_14.mp4',
    video_len = None,
    )

issue_15 = Bunch(
    desc = '誤判料盒為BBOX',    
    vpath= '',
    video_len = None,
    )

issue_16 = Bunch(
    desc = '工具顏色亮度較暗',    
    vpath= '',
    video_len = None,
    )

issue_17 = Bunch(
    desc = '手腕處的黃色手套誤偵測為為TZS',    
    vpath='/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-01 78.69 R11.12_20201017093200-20201017093700_1.mp4',
    video_len = None,
    )

issue_18 = Bunch(
    desc = '工具被手遮擋, 無法用顏色辨識',    
    vpath= '',
    video_len = None,
    )

issue_19 = Bunch(
    desc = '頭套誤判為閃光',    
    vpath='',
    video_len = None,
    )

issue_20 = Bunch(
    desc = '左手作業',    
    vpath= '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-07 78.31 R11.12_20201102132200-20201102132700_20.mp4',
    video_len = None,
    )

issue_21 = Bunch(
    desc = '雙手作業',    
    vpath= '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-07 78.31 R11.12_20201102131100-20201102131600_21.mp4',
    video_len = None,
    )

issue_999 = Bunch(
    desc = 'HMM MODELING',    
    vpath='/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-06 78.26 R11.12_20201029212015-20201029222015_14.mp4',
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
    'issue_19': issue_19,
    'issue_20': issue_20,    
    'issue_21': issue_21,
    'issue_999': issue_999
}

def get_issue_list(echo=True):
    if echo:
        print('\n---- issue list ---\n')
        for k in issue_dict.keys():
            issue = issue_dict.get(k)
            print(f'{k}:', issue.desc, f'({os.path.basename(issue.vpath)})')
    return issue_dict


#------
'''
目前沒有建立demo case lise. 暫時根據PM需求定義case
'''

demo_1 = Bunch(
    desc = '跳過工序5',    
    vpath='/mnt/hdd1/ipcamera_case_data/output/N01-3F 05L F68-02 78.42 R11.12_202010290833.mp4',
    video_len = None,
    )

demo_case_dict={
    'demo_1':demo_1,
}    



