def DIV_PP_P(m1, C1, m2, C2):
    c1_t = C1.copy()
    C = [ [0, 1, [0], 1, [1]] for i in range(m1 - m2 + 1)]
    m = m1 - m2
    for i in range(m + 1):
        C[i] = DIV_QQ_Q(c1_t[i], C2[0])
        l_t, c_t = MUL_PQ_P(m2, C2, C[i])
        l_t, c_t = MUL_Pxk_P(l_t, c_t, m - i)
        m1, c1_t = SUB_PP_P(m1, c1_t, l_t, c_t)
    return [m, C]