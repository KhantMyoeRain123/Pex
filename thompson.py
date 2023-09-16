from collections import deque
from regex_pof import shunting

class TNFA:
    def __init__(self,start_state,final_state,symbol,transitions,states,alphabet) -> None:
        self.start_state=start_state
        self.final_state=final_state
        self.symbol=symbol
        self.transitions=transitions
        self.states=states
        self.alphabet=alphabet

    def __str__(self) -> str:
        out=""
        for t in self.transitions:
            if(t[1]!=""):
                out+="S"+str(t[0])+"-"+t[1]+"-> S"+str(t[2])+"\n"
            else:
                out+="S"+str(t[0])+"-ep-> S"+str(t[2])+"\n"
        return out
#handles state numbering
class TNFAFactory:
    def __init__(self) -> None:
        self.state=0
    def symb_tnfa(self,symbol):
        new_tnfa=TNFA(self.state,self.state+1,symbol,[(self.state,symbol,self.state+1)],[self.state,self.state+1],[symbol])
        self.increment()
        return new_tnfa

    def alt_tnfa(self,tnfa1:TNFA,tnfa2:TNFA):
        new_tnfa=TNFA(self.state,self.state+1,"",tnfa1.transitions+tnfa2.transitions,tnfa1.states+tnfa2.states+[self.state,self.state+1],tnfa1.alphabet+tnfa2.alphabet)
        new_tnfa.transitions.append(
            (new_tnfa.start_state,"",tnfa1.start_state),
        )
        new_tnfa.transitions.append(
            (new_tnfa.start_state,"",tnfa2.start_state),
        )
        new_tnfa.transitions.append(
            (tnfa1.final_state,"",new_tnfa.final_state),
        )
        new_tnfa.transitions.append(
            (tnfa2.final_state,"",new_tnfa.final_state)
        )
        self.increment()
        return new_tnfa

    def concat_tnfa(self,tnfa1:TNFA,tnfa2:TNFA):
        new_tnfa=TNFA(tnfa1.start_state,tnfa2.final_state,"",tnfa1.transitions+tnfa2.transitions,tnfa1.states+tnfa2.states,tnfa1.alphabet+tnfa2.alphabet)
        new_tnfa.transitions.append(
            (tnfa1.final_state,"",tnfa2.start_state)
        )
        return new_tnfa

    def star_tnfa(self,tnfa:TNFA):
        new_tnfa=TNFA(self.state,self.state+1,"",tnfa.transitions,tnfa.states+[self.state,self.state+1],tnfa.alphabet)
        new_tnfa.transitions.append(
            (new_tnfa.start_state,"",tnfa.start_state),
        )
        new_tnfa.transitions.append(
            (tnfa.final_state,"",new_tnfa.final_state)
        )
        new_tnfa.transitions.append(
            (new_tnfa.start_state,"",new_tnfa.final_state)
        )
        new_tnfa.transitions.append(
            (tnfa.final_state,"",tnfa.start_state)
        )
        return new_tnfa

    def plus_tnfa(self,tnfa:TNFA):
        new_tnfa=TNFA(self.state,self.state+1,"",tnfa.transitions,tnfa.states+[self.state,self.state+1],tnfa.alphabet)
        new_tnfa.transitions.append(
            (new_tnfa.start_state,"",tnfa.start_state)
        )
        new_tnfa.transitions.append(
            (tnfa.final_state,"",new_tnfa.final_state)
        )
        new_tnfa.transitions.append(
            (tnfa.final_state,"",tnfa.start_state)
        )
        return new_tnfa

    def increment(self):
        self.state+=2

#thompson construction
def thompson(out_q:deque):
    tnfa_stack=deque()
    factory=TNFAFactory()
    for i in range(len(out_q)):
        c=out_q.popleft()
        if(c.isalpha()):
            s_tnfa=factory.symb_tnfa(c)
            tnfa_stack.append(s_tnfa)
        else:
            if(c=="|"):
                tnfa1=tnfa_stack.pop()
                tnfa2=tnfa_stack.pop()
                a_tnfa=factory.alt_tnfa(tnfa1,tnfa2)
                tnfa_stack.append(a_tnfa)
            elif(c=="?"):
                tnfa1=tnfa_stack.pop()
                tnfa2=tnfa_stack.pop()
                c_tnfa=factory.concat_tnfa(tnfa2,tnfa1)
                tnfa_stack.append(c_tnfa)
            elif(c=="*"):
                tnfa=tnfa_stack.pop()
                star_tnfa=factory.star_tnfa(tnfa)
                tnfa_stack.append(star_tnfa)
            elif(c=="+"):
                tnfa=tnfa_stack.pop()
                p_tnfa=factory.plus_tnfa(tnfa)
                tnfa_stack.append(p_tnfa)

    final_tnfa=tnfa_stack.pop()
    return final_tnfa






