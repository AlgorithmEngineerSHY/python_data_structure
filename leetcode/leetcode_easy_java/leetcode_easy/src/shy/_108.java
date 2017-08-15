package shy;

public class _108 {
	public TreeNode sortedArrayToBST(int[] nums) {
		if (nums.length == 0)
			return null;
		int low = 0, high = nums.length - 1;
		return helper(nums, low, high);
	}

	public TreeNode helper(int[] nums, int low, int high) {
		if (low > high)
			return null;
		int mid = (low + high) / 2;
		TreeNode tree_node = new TreeNode(nums[mid]);
		tree_node.left = helper(nums, low, mid - 1);
		tree_node.right = helper(nums, mid + 1, high);
		return tree_node;
	}
}
