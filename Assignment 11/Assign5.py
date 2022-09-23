def sum_ood_even():
    lst=[15,64,52,53,46,15]
    odd_sum=0
    even_sum=0
    for sub in lst:
        for ele in str(sub):
            if int(ele) % 2==0:
                even_sum +=int(ele)
            else:
                odd_sum += int(ele)
    print("Odd digit sum : " + str(odd_sum))
    print("Even digit sum : " + str(even_sum))
sum_ood_even()

