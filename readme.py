#!/usr/bin/env python
# coding: utf-8

# In[8]:


from csvtomd import md_table
from casedict import get_issue_list#issue_dict, demo_case_dict


# In[9]:


issuelist = get_issue_list()
table = []
for k, case in issuelist.items():
    table.append([k, case.desc, case.vpath])

issue_list_md = md_table(table)
text_file = open('README.md', 'w')
text_file.write(issue_list_md)
text_file.close()


# In[ ]:




