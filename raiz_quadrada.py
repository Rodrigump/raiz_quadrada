def raiz_quadrada(n, precisao=20):

    m = 0 #resultado

    r = n

    ret = ''

    for count in range(precisao):

        i = 0
        j = 0
        k = 0
        while(((20*m + i)*i) <= r):
            j = i
            k = (20*m + j)*j
            i += 1

        m = (10*m) + j

        if(count == 0):
            ret = str(j) + '.'
        else:
            ret = ret + str(j)

        r = (r - k)*100

    return ret

if __name__ == '__main__':

    for i in range(1,11):
        print(f"{i}\t{raiz_quadrada(i)}")