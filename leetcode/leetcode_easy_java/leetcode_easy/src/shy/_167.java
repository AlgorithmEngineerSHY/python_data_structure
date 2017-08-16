package shy;

public class _167 {
	public int[] twoSum(int[] numbers, int target) {
		int[] indice = new int[2];
		int left = 0, right = numbers.length - 1;
		while (true) {
			int tmp = numbers[left] + numbers[right];
			if (tmp == target) {
				indice[0] = left + 1;
				indice[1] = right + 1;
				break;
			} else if (tmp > target) {
				right--;
			} else {
				left++;
			}
		}
		return indice;
	}
}
