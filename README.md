Mondrian
===========================
Mondrian is a Top-down greedy data anonymization algorithm for relational dataset, proposed by Kristen LeFevre in his papers[1]. To our knowledge, Mondrian is the fastest local recording algorithm, which preserve good data utility at the same time. Although LeFevre gave the pseudocode in his papers, the original source code is not available. You can find the third part Java implementation in Anonymization Toolbox[2].

This repository is an **open source python implementation for Mondrian**. I implement this algorithm in python for further study.

### Motivation 
Researches on data privacy have lasted for more than ten years, lots of great papers have been published. However, only a few open source projects are available on Internet [2-3], most open source projects are using algorithms proposed before 2004! Fewer projects have been used in real life. Worse more, most people even don't hear about it. Such a tragedy! 

I decided to make some effort. Hoping these open source repositories can help researchers and developers on data privacy (privacy preserving data publishing).

### Attention

This Mondrian is the earliest Mondrian proposed in [1], which imposes an intuitive ordering on each attribute. So, there is no generalization hierarchies for categorical attributes. This operation brings lower information loss, but worse sematic results. **If you want the Mondrian based on generalization hierarchies, please turn to [Basic_Mondrian](https://github.com/qiyuangong/Basic_Mondrian).**

I used **both adult and INFORMS** dataset in this implementation. For clarification, **we transform NCP to percentage**. This NCP percentage is computed by dividing NCP value with the number of values in dataset (also called GCP[4]). The range of NCP percentage is from 0 to 1, where 0 means no information loss, 1 means loses all information (more meaningful than raw NCP, which is sensitive to size of dataset). 

One more thing!!! Mondrian has strict and relax models. (Most online implementations are in strict model.) Both mondrian split partition with binary split (let lhs and rhs denotes left part and right part). In strict mondrian, lhs has not intersection part with rhs. But in relaxed mondrian, the points in the middle are evenly divided between lhs and rhs to ensure |lhs| = |rhs| (+1 where |partition| is odd). So in relax model, the generalized result of lhs and rhs may have intersection. 

The Final NCP of Mondrian on adult dataset is about 24.91% (relax) and 12.19% (strict), while 12.26% (relax) and 10.21% (strict) on INFORMS data (with K=10).


### Usage and Parameters:
My Implementation is based on Python 2.7 (not Python 3.0). Please make sure your Python environment is collectly installed. You can run Mondrian in following steps: 

1) Download (or clone) the whole project. 

2) Run "anonymized.py" in root dir with CLI.

Parameters:

	# run Mondrian with adult data and default K(K=10)
	python anonymizer.py 
	
	# run Mondrian with adult data K=20
	python anonymized.py a 20

	a: adult dataset, 'i': INFORMS ataset
	k: varying k, qi: varying qi numbers, data: varying size of dataset, one: run only once


### For more information:
[1] K. LeFevre, D. J. DeWitt, R. Ramakrishnan. Mondrian Multidimensional K-Anonymity ICDE '06: Proceedings of the 22nd International Conference on Data Engineering, IEEE Computer Society, 2006, 25

[2] [UTD Anonymization Toolbox](http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home)

[3] [ARX- Powerful Data Anonymization](https://github.com/arx-deidentifier/arx)

[4] G. Ghinita, P. Karras, P. Kalnis, N. Mamoulis. Fast data anonymization with low information loss. Proceedings of the 33rd international conference on Very large data bases, VLDB Endowment, 2007, 758-769

==========================
by Qiyuan Gong
qiyuangong@gmail.com

2015-1-21
