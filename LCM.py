
# coding: utf-8

# In[5]:


def gcd(p,q):
    if p>q:
        a=p
        b=q
    else:
        a=q
        b=p
    r=a%b
    if r==0:
        return b
    else:
        while r!=0:
            c=b%r
            b=r
            r=c
        return b
    
def lcm (p,q):
    g=gcd(p,q)
    lcm=p*q/g
    return int(lcm)
    
    

if __name__ == '__main__':
    input_n = 2
    input_numbers = [int(x) for x in input().split()]
    print(lcm(input_numbers[0],input_numbers[1]))
        
    

