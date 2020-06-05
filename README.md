# text-GCN
- step1 (中文语料处理)
>> ```python process_cnews.py```
- step2 (删除低频词)
>> ```python remove_words.py cnews```
<p align="center"><img src="https://s1.ax1x.com/2020/06/05/ts67e1.png"></p>

- step3 (构建文本图)
>> ```python build_graph.py cnews```
- step4 (训练)
>> ```python train.py cnews```
<p align="center"><img src="https://s1.ax1x.com/2020/06/05/tscJl4.png"></p>

# 感谢原作者
https://github.com/yao8839836/text_gcn
