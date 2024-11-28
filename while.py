# a=2
# while a<=20:
#  print(a)
#  a=a+2
# sum=0
# for a in range(10):
#     sum=sum+a
# print(sum)
    
#print prime number
# prime =1
# if prime > 1:
#  for a in range(13 ):
#     if(prime%1)  ==1:

#      print(prime)
    

#  #print odd number 1to 20   
# a=1
# while a<=20:
#     if(a%2==0):
#      a=a+1
#      continue
#     print(a)
#     a=a+1

    #prime number 1 to 13

for a in range(1,30):
    
    if a>1:
        for i in range(2,a):
            if a% i==0:
                break
        else:

          print(a)
    
        


