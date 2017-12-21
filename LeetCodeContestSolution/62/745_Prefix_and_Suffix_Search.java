'''
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
Note:
words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
'''

class WordFilter {

    Map<String, Integer> map = new HashMap<String, Integer>();

    public WordFilter(String[] words) {

        // generate all the possible pre and suf combinations for each word
        int n = words.length;

        for (int i = 0; i < n; ++i) {

            String word = words[i];
            // all the combinations of prefix and suffix
            int m = word.length();

            for (int j = 0; j <= m; ++j) {
                for (int k = 0; k <= m; ++k) {

                    String prefix = "";
                    if (j > 0) prefix = word.substring(0, j);
                    String suffix = "";
                    if (k < m) suffix = word.substring(k);

                    String key = prefix + "_" + suffix;
                    map.put(key, i);

                }
            }
        }
    }

    public int f(String prefix, String suffix) {

        String key = prefix + "_" + suffix;
        if (map.get(key) == null) return -1;
        else return map.get(key);

    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */
/**