# function3.py

#가변인자처리 *ar 
# *는 Tuple
def union(*ar):
    result = [] 
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result
