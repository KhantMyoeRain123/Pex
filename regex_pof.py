#change infix regex into postfix notation
from collections import deque

def convert(in_s):
    new=''
    for i,c in enumerate(in_s):
        new+=c
        if(i+1<len(in_s)):
            #need to discover more edge cases
            if((c.isalpha() or c=="*" or c=="+") and (in_s[i+1].isalpha() or in_s[i+1]=="(")):
                new+="?"
    return new

def shunting(in_s):
    op_stack = deque()
    out_q=deque()
    mod_in_s=convert(in_s)
    for c in mod_in_s:

        if c.isalpha():
            out_q.append(c)
        else:
            if(c=="|"):
                if(len(op_stack)>0):
                    if(op_stack[-1]=="("):
                        op_stack.append(c)
                    else:
                        while(len(op_stack)>0):
                            out_q.append(op_stack.pop())
                        op_stack.append(c)
                else:
                    op_stack.append(c)
            elif(c=="?"):
                if(len(op_stack)>0):
                    if(op_stack[-1]=="("):
                        op_stack.append(c)
                    else:
                        while(len(op_stack)>0 and (op_stack[-1]=="?" or op_stack[-1]=="*" or op_stack[-1]=="+")):
                            out_q.append(op_stack.pop())

                        op_stack.append(c)
                else:
                    op_stack.append(c)

            elif(c=="*"):
                if(len(op_stack)>0):
                    if(op_stack[-1]=="("):
                        op_stack.append(c)
                    else:
                        while(len(op_stack)>0 and (op_stack[-1]=="*" or op_stack[-1]=="+")):
                            out_q.append(op_stack.pop())
                        
                        op_stack.append(c)
                else:
                    op_stack.append(c)

            elif(c=="+"):
                if(len(op_stack)>0):
                    if(op_stack[-1]=="("):
                        op_stack.append(c)
                    else:
                        while( len(op_stack)>0 and (op_stack[-1]=="*" or op_stack[-1]=="+")):
                            out_q.append(op_stack.pop())
                        
                        op_stack.append(c)
                else:
                    op_stack.append(c)
            
            elif(c=="("):
                op_stack.append(c)
            
            elif(c==")"):
                while(op_stack[-1]!="("):
                    out_q.append(op_stack.pop())
                
                op_stack.pop() #pop off the left parantheses
    while(len(op_stack)>0):
        out_q.append(op_stack.pop())
    
    return out_q



