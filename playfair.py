alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
key = input("Enter the key of the cipher: ")
message = input("Enter the plaintext message: ")

l = []
m = []
n = []
k = []
c = []

def create_list(key,alphabet):  
    for i in key:
        if i not in l:
            l.append(i)

    for i in alphabet:
        if i not in l:
            l.append(i)

    return l

def create_matrix(m,l):
    start = 0
    end = 6

    for i in range(6):
        m.append(l[start:end])
        start = start + 6
        end = end + 6 
    return m

def print_matrix(m):
    for i in m:
        print(i)
    
def create_pair(message,n):
    start = 0   
    while(start+1 <= len(message)):
        if (start+1 == len(message)):
            n.append(message[start] + 'x')
            break
        else:
            if (message[start] != message[start+1]):
                n.append(message[start:start+2])
                start = start + 2
            else:
                n.append(message[start] + 'x')
                start = start + 1

    print("Created Pairs = ",n)


def find_index(m,word):
    for i in range(0,6):
                for j in range(0,6):
                        if m[i][j] == word:
                                return i,j


def join(k):
    z = ''.join(k)
    return z


def encrypt(m,n):
        for i,j in n:
                p1,p2 = find_index(m,i)
                q1,q2 = find_index(m,j)
                if p1 == q1:
                        if p2 < 5 and q2 < 5:
                                k.append(m[p1][p2+1] + m[q1][q2+1])
                        elif p2 == 5 and q2 < 5:
                                k.append(m[p1][1] + m[q2][q2+1])
                        elif p2 < 5 and q2 == 5:
                                k.append(m[p1][p2+1] + m[q2][1])
                else:
                        k.append(m[p1][q2] + m[q1][p2])
        print("Encrpyted message = ",join(k))

def decrypt(m,k):
    for i,j in k:
        p1,p2 = find_index(m,i)
        q1,q2 = find_index(m,j)
        if p1 == q1:
                if p2 < 5 and q2 < 5:
                        c.append(m[p1][p2-1] + m[q1][q2-1])
                elif p2 == 1 and q2 < 5:
                        c.append(m[p1][5] + m[q2][q2-1])
                elif p2 < 5 and q2 == 1:
                        c.append(m[p1][p2-1] + m[q2][5])
        else:
                c.append(m[p1][q2] + m[q1][p2])
    message = join(c)
    print("Decrpyted message = ",message)


create_list(key,alphabet)
create_matrix(m,l)
##print_matrix(m)
create_pair(message,n)
encrypt(m,n)
decrypt = decrypt(m,k)
