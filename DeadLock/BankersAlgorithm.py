import numpy as np
def main():
    data = list(map(int, input().split()))
    n = data[0] #process
    m = data[1] #R.types
    max_claim = np.array([list(map(int, input().split())) for _ in range(n)])
    cur_alloc = np.array([list(map(int, input().split())) for _ in range(n)])
    r_units = data[2:] #R.units
    

    available_units = r_units - cur_alloc.sum(axis=0)
    add_need = max_claim - cur_alloc
    complete = [False]*n
    result = ''
    safe_seq = []

    while(1):
        for idx, p in enumerate(add_need):
            if ((p <= available_units).all() == True and complete[idx] == False):
                available_units = available_units + cur_alloc[idx]
                safe_seq.append(idx + 1)
                complete[idx]=True
                break
            if (idx == n-1):
              if False in complete:
                for i, c in enumerate(complete):
                  if c == False:
                    result = result + "P" + str(i+1) + ' '
                return "This system is Unsafe" + ' beacuse of ' + result
              else:
                for i in safe_seq:
                  result = result + "P" + str(i) + '->'
                return "Safe" + ' | Safe Sequence ' + result[:-2]

print(main())
