a = ["a", "b", "c"]

for i in range(0, 3):   
   for j in range(0, 3):
        for k in range(0, 3):
            if(a[i] != a[j] and a[i] != a[k] and a[j] !=a[k]):
                print(a[i] + a[j] + a[k])
  
   

