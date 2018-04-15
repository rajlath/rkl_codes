public class UniqueDigits
{
    public static int CountNumbersHavingUniqueDigits(int min, int max) {
        int count = 0;

        for (int i = min; i <= max; i++) {
            if (checkUniqueDigits(i)) {
                count++;
            }
        }

        return count;
    }

    public static boolean checkUniqueDigits(int number) {
        int[] appearingDigits = new int[10];
        while (number > 0) {
            int digit = number % 10;
            appearingDigits[digit]++;
            number /= 10;
        }

        for (int i = 0; i < 10; i++) {
            if (appearingDigits[i] > 1) {
                return false;
            }
        }

        return true;
    }
}