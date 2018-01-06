def get_max_palindrome(input1):



public static int lengthofPalindrome(String input1)
{
    String number = input1;i
    Map<Character, Integer> map = new HashMap<>();
    char[] array = null;
    int len = number.length();
    boolean palindrom = false;
    int maxPalindrom = 0;

    for(int j=2; j < len; j +=2)
    {
        for(int i=0; i <= len - j; i++)
        {
            array = number.substring(i, i+j).toCharArray();
            map.clear();
            palindrom = true;
            for(char c : array)
            {
                map.put(c, map.containsKey(c) ? (map.get(c) + 1) : 1);
            }
            for (java.util.Map.Entry<Character, Integer> entry : map.entrySet())
            {
                if(entry.getValue() % 2 != 0){
                    palindrom = false;
                    break;
                }
            }
            if(palindrom)
            {
                maxPalindrom = array.length;
                break;
            }
        }
    }
    return maxPalindrom;
}