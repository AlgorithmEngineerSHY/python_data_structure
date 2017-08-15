package shy;

public class _110 {
	public boolean isBalanced(TreeNode root) {
		if (root == null)
			return true;
		return helper(root) != -1;
	}

	public int helper(TreeNode node) {
		if (node == null)
			return 0;
		int height_left = helper(node.left);
		if (height_left == -1)
			return -1;

		int height_right = helper(node.right);
		if (height_right == -1)
			return -1;
		if (Math.abs(height_right - height_left) > 1)
			return -1;
		return Math.max(height_left, height_right) + 1;

	}
}
