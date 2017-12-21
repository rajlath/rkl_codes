static void Main(string[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        string input = "";
        int n = int.Parse(Console.ReadLine());
        bool isGood = true;
        for (int i = 0; i < n; i++)
        {
            input = AddNode(Console.ReadLine());
            if (!input.Equals("Good"))
            {
                isGood = false;
                break;
            }

        }
        if (!isGood)
        {
            Console.WriteLine("BAD SET");
            Console.WriteLine(input);

        }
        else
        {
            Console.WriteLine("GOOD SET");
        }
        Console.ReadLine();
    }

    private static string AddNode(string input)
    {
        TrieNode tRoot = Root;
        for (int i = 0; i < input.Length; i++)
        {
            if (tRoot.Node.ContainsKey(input[i]))
            {
                tRoot.Node.TryGetValue(input[i], out tRoot);
                if (tRoot.Node.ContainsKey('z'))
                {
                    return input;
                }
            }
            else
            {
                tRoot.Node.Add(input[i], new TrieNode());
                tRoot.Node.TryGetValue(input[i], out tRoot);
            }
        }
        if (!tRoot.Node.Count.Equals(0))
        {
            return input;
        }
        tRoot.Node.Add('z', new TrieNode());
        return "Good";

    }

    public class TrieNode
    {
        public Dictionary<char, TrieNode> Node = new Dictionary<char, TrieNode>();
    }

}