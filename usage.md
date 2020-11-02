# opmovement case list

- History:
  - 0102 - first ver.
  
- Sample Code (pkl mode)


```
from opmovement_caselist.casedict import get_issue_list
issuelist = get_issue_list()
```
  
  
issue_10: 工作檯上有粉紅色PPEN2 (N01-3F 05L F68-06 78.26 R11.12_20201013210000-20201013211000_1.mp4)  
issue_13: 沒有bbox (N01-3F 05L F68-07 78.31 R11.12_202010292220.mp4)  
issue_14: Flash亮度逐漸變大 ()  
issue_15: 誤判料盒為BBOX ()  
issue_16: 工具顏色亮度較暗 ()  
issue_17: 手腕處的黃色手套誤偵測為為TZS (N01-3F 05L F68-01 78.69 R11.12_20201017093200-20201017093700_1.mp4)  
issue_18: 工具被手遮擋, 無法用顏色辨識 ()  
issue_19: 頭套誤判為閃光 ()  
  
  
```
caseid='issue_13'
case = issuelist[caseid]
```


{'desc': '沒有bbox',  
 'vpath': '/mnt/hdd1/ipcamera_case_data/N01-3F 05L F68-07 78.31 R11.12_202010292220.mp4',  
 'video_len': None}  
