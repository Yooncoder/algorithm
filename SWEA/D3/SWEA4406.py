for t in range(1, int(input()) + 1):
    st = list(input())
    a = ['a', 'e', 'i', 'o', 'u']
    n_st = st.copy()
    for i in n_st:
        if i in a:
            st.remove(i)
    print('#{}'.format(t), ''.join(st))