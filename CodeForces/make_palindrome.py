'''
public static String makePalindrome(String base){
    String pref = "";
    int i = base.length() - 1;
    while(! checkPalindrome(pref + base)){
        pref = pref + base.charAt(i);
        i --;
    }
    return pref + base;
}
'''
def is_palindrome(str):
    return str == str[::-1]

ins = input()
ans = ""
i = len(ins) - 1
while not is_palindrome(ans + ins):
    ans+= ins[i]
    i -= 1
print(ans + ins)