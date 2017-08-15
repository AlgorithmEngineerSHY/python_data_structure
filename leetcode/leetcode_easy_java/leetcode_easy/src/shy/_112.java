package shy;

public class _112 {
	public boolean hasPathSum(TreeNode node, int sum) {
		if (node == null)
			return false;
		if (node.left == null && node.right == null) {
			if (node.val == sum)
				return true;
			else
				return false;
		}
		return hasPathSum(node.left, sum - node.val) || hasPathSum(node.right, sum - node.val);
	}

}
