def solution(A, B):
    counter = 0
    N = len(A)
    set_A = set(A)
    set_B = set(B)
    common = set_B.intersection(set_A)
    if len(set_A-common) > N/2:
        counter += N/2
    else:
        counter += len(set_A-common)

    if len(set_B-common) > N/2:
        counter += N/2
    else:
        counter += len(set_B-common)

    counter = min(counter+len(common), N)

    return int(counter)
