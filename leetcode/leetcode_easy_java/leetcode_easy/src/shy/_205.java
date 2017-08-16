package shy;

public class _205 {
	public boolean isIsomorphic(String s, String t) {
		int[] a = new int[127];
		int[] b = new int[127];
		int n = s.length();
		for (int i = 0; i < n; i++) {
			if(a[s.charAt(i)]!=b[t.charAt(i)]) {
				return false;
			}else {
				a[s.charAt(i)]=i+1;
				b[t.charAt(i)]=i+1;
			}
		}
		return true;
	}
}
