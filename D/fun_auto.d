import std.stdio : writeln;
import std.random : uniform;

void random_calculator()
{
    auto add(int lhs, int rhs){
        return lhs + rhs;
    }

    int a = 10;
    int b =  5;
    writeln(add(a, b));
}

void main()
{
    random_calculator();
}
