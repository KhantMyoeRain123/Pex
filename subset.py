from collections import deque
from thompson import TNFA,thompson

#BFS
def epsilon_closure(state,tnfa:TNFA):
    closure_list=[]
    worklist=deque()
    closure_list.append(state)
    worklist.append(state)
    while(len(worklist)>0):
        s=worklist.popleft()
        for transition in tnfa.transitions:
            if(transition[0]==s and transition[1]==""):
                closure_list.append(transition[2])
                worklist.append(transition[2])
    return closure_list



def delta(state,c):
    pass

def subset(tnfa:TNFA):
    Q=[] #subsets of nfa states
    T=[] #dictionary of transitions
    worklist=deque()
    q0=epsilon_closure(tnfa.start_state)
    worklist.append(q0)

    while(len(worklist)>0):
        q=worklist.popleft()
        for c in tnfa.alphabet:
            t=epsilon_closure(delta(q,c))
            T.append((q,c,t))
            if t not in Q:
                Q.append(t)
                worklist.append(t)

    return (Q,T)

def to_dfa(Q,T):
    pass


