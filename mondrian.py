

global_QID_len = 10
global_K = 0





def NCP(partition, index):
    """
    """


    return 



def choose_dimension(partition):
    """chooss dim with largest ncp
    """
    max_ncp = 0
    max_dim = -1
    for i in range(global_QID_len):
        ncp = NCP(partition, i)
        if ncp > max_ncp:
            max_ncp = ncp
            max_dim = i
    if max_dim != -1:
        return max_dim


def frequency_set(partition, dim):
    """get the frequency_set of partition on dim
    """
    value_set = set()
    frequency = {}
    for record in partition:
        if record[dim] in value_set:
            frequency[record[dim]] ++
        else:
            frequency[record[dim]] = 1
    return (value_set, frequency_set)


def find_median(fs):
    """find the middle of the partition, return splitVal
    """
    splitVal = ''
    value_list = fs[0]
    frequency = fs[1]
    total = sum(frequency.keys())
    middle = total / 2
    if middle < global_K:
        return ''
    index = 0
    for t in value_list:
        if index < middle:
            index += frequency[t]
            splitVal = t
            break
    else:
        print "Error: cannot find splitVal"
    return splitVal


def mondrian():
    """
    """
    global global_K, global_QID_len
    dim = choose_dimension(partition)
    fs = frequency_set(partition, dim)
    value_list = list(fs[0])
    sort(value_list, cmp=node_cmp)
    fs[0] = value_list
    splitVal = find_median(fs)
    index = value_list.index(splitVal)



    lhs = 0 <= 
    rhs = 0 >

    return mondrian(rhs) U mondrian(lhs)