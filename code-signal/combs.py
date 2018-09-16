'''
static int combs(string comb1, string comb2)
        {
            //int c1 = comb1.Select((c, i) => (c == '*' ? 1 : 0) << i).Sum();
            //int c2 = comb2.Select((c, i) => (c == '*' ? 1 : 0) << i).Sum();
            //var s = Enumerable.Range(0, 32).First(i => (c1 | (c2 << i)) == (c1 + (c2 << i)));
            //return Math.Max(comb1.Length, comb2.Length + s);

            int best = comb1.Length + comb2.Length;
            for (int i = -comb2.Length; i <= comb1.Length; ++i)
            {
                bool fits = true;
                for (int j = 0; j < comb2.Length; ++j)
                {
                    int k = i + j;
                    if (k >= 0 && k < comb1.Length && comb1[k] == '*' && comb2[j] == '*') fits = false;
                }
                if (!fits) continue;
                int width = Math.Max(comb1.Length, i + comb2.Length) - Math.Min(i, 0);
                if (width < best) best = width;
            }
            return best;
'''
def combs(comb1, comb2):
    best = len(comb1) + len(comb2)
    for i in range(-len(comb2), len(comb1) + 1):
         fits = True
         for j in range(len(comb2)):
             k = i + j
             if k >= 0 and k < len(comb1) and comb1[k] == "*" and comb2[j] == "*":
                 fits = False
         if not fits: continue;
         width = max(len(comb1), i + len(comb2)) - min(i, 0)
         if width < best: best = width
    return best

print(combs("*..*" ,"*.*"))




