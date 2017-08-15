package shy;

public class _125 {
	public boolean isPalindrome(String s) {
		String actual = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
		String rev = new StringBuilder(actual).reverse().toString();
		return rev.equals(actual);
	}
}
