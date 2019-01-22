void main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    int a[n];
    int i;
    for (i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
    }
    while (q--)
    {
        int s, l, r;
        scanf("%d", &s);
        if (s == 1)
        {
            scanf("%d", &l);
            if (a[l] == 1)
            {
                a[l] = 0;
            }
            else
            {
                a[l] = 1;
            }
        }
        else
        {
            scanf("%d %d", &l, &r);
            if (a[l] == 1)
            {
                printf("ODD\n");
            }
            else
            {
                printf("EVEN\n");
            }
        }
    }
}