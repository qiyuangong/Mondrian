Mondrian
===========================
Mondrian is a Top-down greedy algorithm data anonymization algorithm for relational dataset, proposed by Kristen LeFevre in his papers[1]. To our knowledge, Mondrian is the fastest local recording algorithm, which preserve good data utility at the same time. Although LeFevre gave the pseudocode in his papers, the original source code is not available. You can find the Java implement in Anonymization Toolbox[2].

This repository is an *open source python implement* for Mondrian. I implement this algorithm in python for further study.

## Attention
I used INFORMS dataset instead of Adults data in this implement. Because attributes in Adults data are almost categorical. I found it difficult to convert them to numeric, meanwhile this transformation will bring huge information loss. So I use INFORMS dataset, which is total numeric. The Final NCP of Mondrian on INFORMS dataset is about 9.54% (Nice result!).

### Motivation 
Researches on data privacy have lasted for more than ten years, lots of great papers have been published. However, only a few open source projects are available on Internet [2-3], most open source projects are using algorithms proposed before 2004! Fewer projects have been used in real life. Worse more, most people even don't hear about it. Such a tragedy! 

I decided to make some effort. Hoping these open source repositories can help researchers and developers on data privacy (privacy preserving data publishing).

## For more information:
[1] K. LeFevre, D. J. DeWitt, R. Ramakrishnan. Mondrian Multidimensional K-Anonymity ICDE '06: Proceedings of the 22nd International Conference on Data Engineering, IEEE Computer Society, 2006, 25

[2] [UTD Anonymization Toolbox](http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home)

[3] [ARX- Powerful Data Anonymization](https://github.com/arx-deidentifier/arx)

==========================
by Qiyuan Gong
qiyuangong@gmail.com

2015-1-21
