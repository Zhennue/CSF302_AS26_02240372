import random, csv
from pathlib import Path

def select_activities(items, rule='finish'):
    keys={'finish':lambda x:(x[1],x[0]), 'start':lambda x:(x[0],x[1]), 'duration':lambda x:(x[1]-x[0],x[0])}
    chosen=[]; last=-1
    for a in sorted(items,key=keys[rule]):
        if a[0]>=last: chosen.append(a); last=a[1]
    return chosen

def find_counterexamples(seed=372):
    r=random.Random(seed); found={'start':None,'duration':None}
    for _ in range(20000):
        items=[]
        for _ in range(r.randint(5,9)):
            s=r.randint(0,15); items.append((s,r.randint(s+1,s+8)))
        opt=select_activities(items,'finish')
        for rule in found:
            got=select_activities(items,rule)
            if found[rule] is None and len(got)<len(opt): found[rule]=(items,got,opt)
        if all(found.values()): break
    return found

def fractional_knapsack(items, capacity):
    chosen=[]; total=0
    for name,value,weight in sorted(items,key=lambda x:x[1]/x[2],reverse=True):
        fraction=min(1,capacity/weight)
        if fraction<=0: break
        chosen.append((name,fraction)); total+=value*fraction; capacity-=weight*fraction
    return total,chosen

def greedy01(items, capacity):
    total=0
    for value,weight in sorted(items,key=lambda x:x[0]/x[1],reverse=True):
        if weight<=capacity: total+=value; capacity-=weight
    return total

def dp01(items, capacity):
    dp=[0]*(capacity+1)
    for value,weight in items:
        for w in range(capacity,weight-1,-1): dp[w]=max(dp[w],dp[w-weight]+value)
    return dp[capacity]

def compare(trials=1000,seed=372):
    r=random.Random(seed); worst=1; avg=0; case=None
    for _ in range(trials):
        items=[(r.randint(5,100),r.randint(1,30)) for _ in range(r.randint(5,12))]; cap=r.randint(10,60)
        g=greedy01(items,cap); opt=dp01(items,cap); ratio=g/opt if opt else 1
        avg+=ratio
        if ratio<worst: worst=ratio; case=(items,cap,g,opt)
    return worst,avg/trials,case

if __name__=='__main__':
    acts=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    print('Q1.1 Activity selection:',acts)
    for rule in ('finish','start','duration'): print(rule,select_activities(acts,rule))
    print('\nQ1.2 Random counterexamples')
    for rule,result in find_counterexamples().items():
        print('\nRule:',rule)
        if result: print('Input:',result[0],'\nGreedy:',result[1],len(result[1]),'\nEarliest finish:',result[2],len(result[2]))
        else: print('No counterexample found')
    items=[('A',60,10),('B',100,20),('C',120,30)]
    value,chosen=fractional_knapsack(items,50)
    print('\nQ1.3 Fractional knapsack:',items,'capacity=50','chosen=',chosen,'value=',value)
    worst,avg,case=compare()
    print('\nQ1.4 Greedy vs DP 0/1 knapsack: 1000 random trials')
    print(f'Worst greedy/optimal ratio: {worst:.4f} ({worst*100:.2f}%)')
    print(f'Average ratio: {avg:.4f}')
    print('Worst case (items, capacity, greedy, optimal):',case)
    out=Path(__file__).parent/'outputs'/'q1_knapsack_summary.csv'
    with out.open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['trials','worst_ratio','average_ratio']); w.writerow([1000,worst,avg])
    print('Saved',out)
