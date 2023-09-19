from thompson import thompson
from subset import subset,to_dfa
from regex_pof import shunting


out_q=shunting("a|bc")
tnfa=thompson(out_q)
print(tnfa)
print(tnfa.final_state)
Q,T=subset(tnfa)
print("Q:",Q)
print("T:",T)
dfa=to_dfa(tnfa,Q,T)
print(dfa.states)
print(dfa.start_state)
print(dfa.final_states)
print(dfa.transitions)