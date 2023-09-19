from collections import deque
from thompson import TNFA
import collections

class DFA:
    def __init__(self,start_state,final_states,transitions,states,alphabet) -> None:
        self.start_state=start_state
        self.final_states=[]
        self.transitions={}
        self.alphabet=[]
        self.states=[]
        


#BFS
def epsilon_closure(state,tnfa:TNFA):
    if(state==-1):
        return []
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



def delta(state_list,c,tnfa:TNFA):
    for state in state_list:
        for transition in tnfa.transitions:
            if(transition[0]==state and transition[1]==c):
                return transition[2]
    return -1 #for completeness although this never happens with epsilon closure




def subset(tnfa:TNFA):
    Q=[] #subsets of nfa states
    T=[] #dictionary of transitions
    worklist=deque()
    q0=epsilon_closure(tnfa.start_state,tnfa)
    Q.append(q0)
    worklist.append(q0)

    while(len(worklist)>0):
        q=worklist.popleft()
        for c in tnfa.alphabet:
            t=epsilon_closure(delta(q,c,tnfa),tnfa)
            if(len(t)==0):
                continue
            T.append((q,c,t))
            if t not in Q:
                Q.append(t)
                worklist.append(t)

    return (Q,T)

def to_dfa(tnfa:TNFA,Q,T):
    dfa=DFA(0,[],{},[],tnfa.alphabet)
    dfa.transitions=collections.defaultdict(dict)
    for i in range(len(Q)):
        dfa.states.append(i)
    for i in range(len(Q)):
        if(tnfa.final_state in Q[i]):
            dfa.final_states.append(dfa.states[i])
        for transition in T:
            if(transition[0]==Q[i]):
                dfa.transitions[i][transition[1]]=Q.index(transition[2])
    
    dfa.transitions=dict(dfa.transitions)
    return dfa






