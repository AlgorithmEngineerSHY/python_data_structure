package shy;

public class _111 {
	public int minDepth(TreeNode root) {
		if (root == null)
			return 0;
		int height_left = minDepth(root.left);
		int height_right = minDepth(root.right);
		if (height_left == 0)
			return height_right + 1;
		if (height_right == 0)
			return height_left + 1;
		return Math.min(height_left, height_right) + 1;
	}
}
