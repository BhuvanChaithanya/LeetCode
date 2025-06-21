class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = defaultdict(int)

        for n in bills:

            if n == 5:
                hashmap[n] +=1

            elif n==10:
                if hashmap[5]<1:
                    return False

                else:
                    hashmap[5] -=1
                hashmap[10] +=1

            elif n == 20:
                if ((hashmap[5]<3) and (hashmap[10]<1 or hashmap[5]<1)):
                    return False
                elif (hashmap[10]>=1 and hashmap[5]>=1):
                    hashmap[10] -=1
                    hashmap[5] -=1

                else:
                    hashmap[5] -=3
        return True