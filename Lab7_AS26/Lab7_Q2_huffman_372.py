import heapq
from collections import Counter
from pathlib import Path

class Node:
    def __init__(self,ch=None,left=None,right=None): self.ch,self.left,self.right=ch,left,right

def build_tree(text):
    freq=Counter(text); heap=[]
    for order,(ch,count) in enumerate(freq.items()): heapq.heappush(heap,(count,order,Node(ch)))
    if not heap: return None,freq
    if len(heap)==1: return heap[0][2],freq
    order=len(heap)
    while len(heap)>1:
        fa,_,a=heapq.heappop(heap); fb,_,b=heapq.heappop(heap)
        heapq.heappush(heap,(fa+fb,order,Node(None,a,b))); order+=1
    return heap[0][2],freq

def codes_for(root):
    codes={}
    def walk(node,prefix):
        if node is None:return
        if node.ch is not None: codes[node.ch]=prefix or '0'
        else: walk(node.left,prefix+'0'); walk(node.right,prefix+'1')
    walk(root,''); return codes

def encode(text,codes): return ''.join(codes[c] for c in text)
def decode(bits,root):
    if root is None:return ''
    if root.ch is not None:return root.ch*len(bits)
    out=[]; node=root
    for bit in bits:
        node=node.left if bit=='0' else node.right
        if node.ch is not None: out.append(node.ch); node=root
    return ''.join(out)

def analyse(path):
    text=path.read_text(encoding='utf-8'); root,freq=build_tree(text); codes=codes_for(root)
    bits=encode(text,codes); restored=decode(bits,root); assert restored==text
    fixed=len(text.encode('utf-8'))*8
    ratio=len(bits)/fixed if fixed else 0
    print(f'\nFile: {path.name} | characters: {len(text)}')
    print('Character | Frequency | Huffman code')
    for ch in sorted(freq): print(f'{repr(ch):10} | {freq[ch]:9} | {codes[ch]}')
    print('Huffman payload bits:',len(bits),'| fixed 8-bit bytes:',fixed)
    print(f'Payload ratio: {ratio:.4f} | space saved: {(1-ratio)*100:.2f}%')
    print('Decode verification:', 'PASSED' if restored==text else 'FAILED')

if __name__=='__main__':
    base=Path(__file__).parent
    print('Q2 Huffman coding')
    for name in ('sample_text_1.txt','sample_text_2.txt','sample_text_3.txt'): analyse(base/name)
