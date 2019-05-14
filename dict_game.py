import pickle

def choice(dct):
    str_1 = list(dct.keys())
    print ('Choose from : ' + ', '.join(str_1))
    in1 = input()
    if in1 not in str_1:
        print('Please, try again')
        in1=choice(dct)
        return str(in1)
    else:
        return str(in1)

def prover(str1,dct):
    if type(dct.get(str1)) == str :
        st = (dct,str1)
        return st
    else :
        dct1=dct.get(str1)
        str2 = choice(dct1)
        st1 = prover(str2,dct1)
        return st1
    
def new_item(che,r):
    print ('Set new key for '+str(r))
    c3 = input()
    if c3 ==che:
        print('Such key already exists. Try again')
        ch = new_item(che,r)
        return ch
    else:
        return c3
    

def question(prompt):
    return input(prompt).lower()
    
def main(prompt = 'Do you want to play again? [y/n] '):
    inp = None
    while inp != 'n':
        with open('dump.txt', 'rb') as f:
            dct = pickle.load(f)
        #dct = {'person':{'boy':'Dan','girl':'Kate'},'animal':'parrot'}
        stro = choice(dct)
        key1=prover(stro,dct)
        dct_cop = key1[0]
        res = dct_cop.get(key1[1])
        print ('Is it '+str(res)+'? [yes/no]')
        ch = input()
        if ch == 'no': 
            print('Who is it?')
            ch1 = input()
            print('Set new key for '+str(ch1))
            ch2 = input()
            ch3=new_item(ch2,res)
            db_n = {ch3:res, ch2:ch1}
            db_new = {key1[1]:db_n}
            dct_cop.update(db_new)
            print ('Thank you, dictionary was updated')
        else:
            print ('Bingo!')
        with open('dump.txt', 'wb') as f:
            pickle.dump(dct, f)
        inp = question(prompt)
    else:
        print ('Bye!')
main()   
