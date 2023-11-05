class Solution:
    """
    @param key: A string you should hash
    @param h_a_s_h__s_i_z_e: An integer
    @return: An integer

    description: In data structure Hash, hash function is used to convert 
    a string(or any other type) into an integer smaller than hash size 
    and bigger or equal to zero. The objective of designing a hash function is to "hash" 
    the key as unreasonable as possible. 
    A good hash function can avoid collision as less as possible. 
    A widely used hash function algorithm is 
    using a magic number 33, consider any string as a 33 based big integer

    Input:  key="abcd", size = 1000
    Output: 978
    Explanation: (97*33^3 + 98*33^2 + 99*33 + 100*1)%1000 = 978

    Input:  key="abcd", size = 100
    Output: 78
    Explanation: (97*33^3 + 98*33^2 + 99*33 + 100*1)%100 = 78

    """
    def hash_code(self, key: str, h_a_s_h__s_i_z_e: int) -> int:
        # write your code here
        print(ord("a")) # --> this gives ASCII value of a char in python

        result = 0
        n = len(key)

        for idx, each_char in enumerate(key):
            char_val = ord(each_char) * pow(33, n - idx-1)
            # print(ord(each_char), n - idx -1 )
            result = result + char_val
            
        print(result % h_a_s_h__s_i_z_e)
        return result % h_a_s_h__s_i_z_e
    def hash_code02(self, key: str, h_a_s_h__s_i_z_e: int) -> int:
        result = 0
        n = len(key)
        powers_of_33 = [33 ** (n - idx - 1) for idx in range(n)]
        char_values = [ord(each_char) for each_char in key]

        for idx in range(n):
            char_val = char_values[idx] * powers_of_33[idx]
            result += char_val

        return result % h_a_s_h__s_i_z_e
    
    def hash_code03(self, key: str, h_a_s_h__s_i_z_e: int) -> int:
        # write your code here
        ans = 0
        for x in key:
            ans = (ans * (33 % h_a_s_h__s_i_z_e) + ord(x)) % h_a_s_h__s_i_z_e     
        return ans
    
new_solution = Solution()
key="abcd"
size = 1000
result = new_solution.hash_code03(key, size)
print("result", result)