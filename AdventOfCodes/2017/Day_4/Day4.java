

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import util.ReadInputHelper;
import java.io.BufferedReader;
import java.io.FileReader;


public class Day4 {
	public static void main(String[] args) {
		ArrayList<String> lines = new ArrayList<>();
		try {
			BufferedReader br = new BufferedReader(new FileReader("input.txt"));
			try {
				String line = br.readLine();

				while (line != null) {
					lines.add(line);
					line = br.readLine();
				}
			} finally {
				br.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		//ArrayList<String> lines = new ReadInputHelper(4).getLines();
		int sum = 0;
		for (int i = 0; i < lines.size(); i++) {
			HashSet<String> set = new HashSet<>();

			String[] words = lines.get(i).split(" ");

			for (int k = 0; k < words.length; k++) {
				char[] temp2 = words[k].toCharArray();
				Arrays.sort(temp2);

				set.add(new String(temp2));
			}

			if (set.size() == words.length)
				sum += 1;
		}

		System.out.println(sum);
	}
}
