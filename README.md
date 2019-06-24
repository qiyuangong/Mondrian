Mondrian [![Build Status](https://travis-ci.org/qiyuangong/Mondrian.svg?branch=master)](https://travis-ci.org/qiyuangong/Mondrian)
===========================
Mondrian is a Top-down greedy data anonymization algorithm for relational dataset, proposed by Kristen LeFevre in his papers[1]. To our knowledge, Mondrian is the fastest local recording algorithm, which preserve good data utility at the same time. Although LeFevre gave the pseudocode in his papers, the original source code is not available. You can find the third part Java implementation in Anonymization Toolbox[2].

This repository is an **open source python implementation for Mondrian**.

### Motivation
Researches on data privacy have lasted for more than ten years, lots of great papers have been published. However, only a few open source projects are available on Internet [2-3], most open source projects are using algorithms proposed before 2004! Fewer projects have been used in real life. Worse more, most people even don't hear about it. Such a tragedy!

I decided to make some effort. Hoping these open source repositories can help researchers and developers on data privacy (privacy preserving data publishing, data anonymization).

### Attention

This Mondrian is the earliest Mondrian proposed in [1], which imposes an intuitive ordering on each attribute. So, there is no generalization hierarchies for categorical attributes. This operation brings lower information loss, but worse semantic results. **If you want the Mondrian based on generalization hierarchies, please turn to [Basic_Mondrian](https://github.com/qiyuangong/Basic_Mondrian).**

I used **both adult and INFORMS** dataset in this implementation. For clarification, **we transform NCP (Normalized Certainty Penalty) to percentage**. This NCP percentage is computed by dividing NCP value with the number of values in dataset (also called GCP (Global Certainty Penalty) [4]). The range of NCP percentage is from 0 to 1, where 0 means no information loss, 1 means loses all information (more meaningful than raw NCP, which is sensitive to size of dataset).

One more thing!!! Mondrian has strict and relax models. (Most online implementations are in strict model.) Both Mondrian split partition with binary split (let lhs and rhs denotes left part and right part). In strict Mondrian, lhs has not intersection part with rhs. But in relaxed Mondrian, the points in the middle are evenly divided between lhs and rhs to ensure `|lhs| = |rhs|` (+1 where `|partition|` is odd). So in relax model, the generalized result of lhs and rhs may have intersection.

The Final NCP of Mondrian on [adult dataset](https://archive.ics.uci.edu/ml/datasets/adult) is about 24.91% (relax) and 12.19% (strict), while 12.26% (relax) and 10.21% (strict) on [INFORMS data](https://sites.google.com/site/informsdataminingcontest/) (with K=10).

### Basic idea of Mondrian
#### First, what is k-anonymity?
Assuming your record is in this format: [QID, SA]. QID means quasi-identifier such as age and birthday, SA means sensitive information such as disease information. The basic idea of k-anonymity is `safety in group` (or safety in numbers [5]), which means that you are safe if you are in a group of people whose QIDs are the same. Note nobody can infer your sensitive information (SA) from this group using QID, as shown in Fig. 1 (k=3 in 1(b) and 1(c)). If each of these group has at least k people, then this dataset satisfy k-anonymity.

<p align="center">
<img src=https://cloud.githubusercontent.com/assets/3848789/25949050/c6a7e8ec-3688-11e7-933d-d5a991e6ef30.png width=750>
</p>
<p align="center">
Figure 1. Anonymity, Privacy and Generalization
</p>

**But in practice, the raw datasets usually don't satisfy k-anonymity, as shown in Fig. 1(a).** So, we need some help from anonymization algorithm to transform the raw datasets to anonymized datasets. Mondrian is one of them, and it is based on generalization. I don't want to talk too much about generalization. In a word, generalization is a kind of transformation, which finds a result QID* that covers all QIDs (QID1~QID3 in Fig. 1 (b)). And it also brings information loss (distortion).

#### How Mondrian anonymizes dataset?
Here is the basic workflow of Mondrian:

1. Partition the raw dataset into k-groups using kd-tree. k-groups means that each group contains at least k records.
2. Generalization each k-group (Fig. 1(b)), such that each group has the same QID*.

Why using kd-tree? Because it is fast, straight-forward and sufficient.

<p align="center">
<img src=https://cloud.githubusercontent.com/assets/3848789/25949051/c6a87622-3688-11e7-8bd0-726f07245570.png width=750>
</p>
<p align="center">
Figure 2. Basic workflow of Modnrian
</p>

<p align="center">
<img src=https://cloud.githubusercontent.com/assets/3848789/25949052/c6ab3fce-3688-11e7-99ea-cde7bccd8684.png width=450>
</p>
<p align="center">
Figure 3. kd-tree
</p>


### Usage and Parameters:
The Implementation is based on Python 3 and compatible with python 2.7. You can run Mondrian in following steps:

1) Download (or clone) the whole project.

2) Run `anonymized.py` in root dir with CLI.

3) Get the anonymized dataset from `data/anonymized.data`, if you didn't add `[k | qi | data]`.

Parameters:

	# Usage: python anonymizer.py [r|s] [a | i] [k | qi | data]
	# r: relax mondrian, s: strict mondrian
	# a: adult dataset, 'i': INFORMS dataset
	# k: varying k, qi: varying qi numbers, data: varying size of dataset
	# run Mondrian with adult data and default K (K=10)
	python anonymizer.py

	# run Strict Mondrian with adult data K=20
	python anonymizer.py s a 20

	# run Relax Mondrian with INFORMS data K=11
	python anonymizer.py r i 1


	# Evluating Strict Mondrian with k on adult data
	python anonymizer.py s a k


### For more information:
[1] K. LeFevre, D. J. DeWitt, R. Ramakrishnan. Mondrian Multidimensional K-Anonymity ICDE '06: Proceedings of the 22nd International Conference on Data Engineering, IEEE Computer Society, 2006, 25

[2] [UTD Anonymization Toolbox](http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home)

[3] [ARX- Powerful Data Anonymization](https://github.com/arx-deidentifier/arx)

[4] G. Ghinita, P. Karras, P. Kalnis, N. Mamoulis. Fast data anonymization with low information loss. Proceedings of the 33rd international conference on Very large data bases, VLDB Endowment, 2007, 758-769

[5] Y. He, J. F. Naughton, Anonymization of set-valued data via top-down, local generalization. Proceedings of VLDB, 2009, 2, 934-945

### Support

- You can post bug reports and feature requests at the [Issue Page](https://github.com/qiyuangong/Mondrian/issues).
- Contributions via [Pull request](https://github.com/qiyuangong/Mondrian/pulls) is welcome.
- Also, you can contact me via [email](mailto:qiyuangong@gmail.com).

==========================

by [Qiyuan Gong](mailto:qiyuangong@gmail.com)

2017-5-23


### Contributor List 🏆
* [Qiyuan Gong](mailto:qiyuangong@gmail.com)
* [Liu Kun](https://github.com/build2last)
