
# Задача P-13: " Преобразование многочлена — кратные корни в простые"
# Здех К.В.

def NMR_P_P(k,arr):
    z,m = DER_P_P(k,arr)
    u,t = GCF_PP_P(k,arr,z,m)
    j,l = DIV_PP_P(k,arr,u,t)
    return [j,l]
