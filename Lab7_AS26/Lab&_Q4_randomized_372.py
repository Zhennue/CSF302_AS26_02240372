import random, time, csv
from pathlib import Path

def quickselect(values,k,rng=None):
    if not 1<=k<=len(values):raise ValueError('k out of range')
    a=list(values); target=k-1; left=0; right=len(a)-1; rng=rng or random.Random()
    while left<=right:
        p=rng.randint(left,right); pivot=a[p]; a[p],a[right]=a[right],a[p]; store=left
        for i in range(left,right):
            if a[i]<pivot:a[store],a[i]=a[i],a[store];store+=1
        a[store],a[right]=a[right],a[store]
        if store==target:return a[store]
        if target<store:right=store-1
        else:left=store+1
    raise RuntimeError('selection failed')

def quickselect_benchmark():
    rng=random.Random(372); rows=[]
    for n in (10_000,100_000,1_000_000):
        values=[rng.randrange(n*10) for _ in range(n)]; k=n//2
        t=time.perf_counter(); value=quickselect(values,k,random.Random(n)); qt=time.perf_counter()-t
        t=time.perf_counter(); sorted_value=sorted(values)[k-1]; st=time.perf_counter()-t
        assert value==sorted_value
        print(f'n={n:,}: quickselect={qt:.4f}s | sort+index={st:.4f}s | kth value={value}')
        rows.append([n,k,qt,st,value])
    out=Path(__file__).parent/'outputs'/'q4_quickselect_benchmark.csv'
    with out.open('w',newline='') as f:w=csv.writer(f);w.writerow(['n','k','quickselect_seconds','sort_index_seconds','kth_value']);w.writerows(rows)
    print('Saved',out)

def miller_rabin(n,rounds=10,rng=None):
    if n<2:return False
    if n%2==0:return n==2
    if n==3:return True
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    rng=rng or random.Random()
    for _ in range(rounds):
        a=rng.randrange(2,n-1); x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=pow(x,2,n)
            if x==n-1:break
        else:return False
    return True

def trial_division(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def compare_primes():
    rng=random.Random(372); rows=[]; agree=0
    nums=[rng.randrange(100_000_000_001,999_999_999_999)|1 for _ in range(20)]
    for n in nums:
        t=time.perf_counter(); mr=miller_rabin(n,10,random.Random(n)); mt=time.perf_counter()-t
        t=time.perf_counter(); td=trial_division(n); tt=time.perf_counter()-t
        agree+=mr==td; rows.append([n,mr,td,mt,tt])
        print(f'{n}: Miller-Rabin={mr}, trial division={td}, MR={mt:.6f}s, trial={tt:.6f}s')
    out=Path(__file__).parent/'outputs'/'q4_primality_comparison.csv'
    with out.open('w',newline='') as f:w=csv.writer(f);w.writerow(['number','miller_rabin','trial_division','mr_seconds','trial_seconds']);w.writerows(rows)
    print(f'Agreement: {agree}/20. Saved {out}')

def carmichael_experiment():
    rng=random.Random(561); prime=sum(miller_rabin(561,1,rng) for _ in range(1000))
    print('\nCarmichael 561, one Miller-Rabin round, 1000 runs')
    print('Reported prime:',prime,'| reported composite:',1000-prime)

if __name__=='__main__':
    print('Q4.1 Randomized Quickselect vs sorting');quickselect_benchmark()
    print('\nQ4.2 Miller-Rabin vs trial division on 20 random 12-digit odd numbers');compare_primes()
    print('\nQ4.3 Carmichael experiment');carmichael_experiment()
