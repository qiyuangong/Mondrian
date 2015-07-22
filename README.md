Mondrian
===========================
Mondrian is a Top-down greedy algorithm data anonymization algorithm for relational dataset, proposed by Kristen LeFevre in his papers[1]. To our knowledge, Mondrian is the fastest local recording algorithm, which preserve good data utility at the same time. Although LeFevre gave the pseudocode in his papers, the original source code is not available. You can find the Java implement in Anonymization Toolbox[2].

This repository is an *open source python implement* for Mondrian. I implement this algorithm in python for further study.

## Attention
I used both adult and INFORMS dataset in this implementation. For cleaification, **we transform NCP to percentage**, making the information loss more meaningful (NCP=2000 v.s. NCP=20%). This NCP percentage is compute by NCP value divided by the number of values in dataset. The Final NCP of Mondrian on adult dataset is about 12.19% (Nice result!), while 10.21% on INFORMS data (with K=10).

### Motivation 
Researches on data privacy have lasted for more than ten years, lots of great papers have been published. However, only a few open source projects are available on Internet [2-3], most open source projects are using algorithms proposed before 2004! Fewer projects have been used in real life. Worse more, most people even don't hear about it. Such a tragedy! 

I decided to make some effort. Hoping these open source repositories can help researchers and developers on data privacy (privacy preserving data publishing).

### Usage:
My Implement is based on Python 2.7 (not Python 3.0). Please make sure your Python environment is collect installed. You can run Mondrian in following steps: 
1) Download (or clone) the whole project. 2) Run "anonymized.py" in root dir with CLI.


	# run Mondrian with adult data and default K(K=10)
	python anonymizer.py 
	
	# run Mondrian with adult data K=20
	python anonymized.py a 20

Parameters:

	a: adult dataset, 'i': INFORMS ataset
	k: varying k, qi: varying qi numbers, data: varying size of dataset, one: run only once


## For more information:
[1] K. LeFevre, D. J. DeWitt, R. Ramakrishnan. Mondrian Multidimensional K-Anonymity ICDE '06: Proceedings of the 22nd International Conference on Data Engineering, IEEE Computer Society, 2006, 25

[2] [UTD Anonymization Toolbox](http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home)

[3] [ARX- Powerful Data Anonymization](https://github.com/arx-deidentifier/arx)

==========================
by Qiyuan Gong
qiyuangong@gmail.com

2015-1-21
