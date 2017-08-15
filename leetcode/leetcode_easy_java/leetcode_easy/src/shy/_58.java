package shy;

public class _58 {
	public int lengthOfLastWord(String s) {
		return s.trim().length() - s.trim().lastIndexOf(' ') - 1;
	}
}
