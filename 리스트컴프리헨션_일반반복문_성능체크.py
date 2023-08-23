def a():
    result = []
    for i in range(10000):
        result.append(i)
    return result


def b():
    return [i for i in range(10000)]


#직접 이 모듈을 실행한 경우만 실해 (entry point)
if __name__ == '__main__':
    import timeit
    print("---for in---")    
    print(timeit.timeit("a()", number=100, globals=globals()))
    print(timeit.timeit("b()", number=100, globals=globals()))