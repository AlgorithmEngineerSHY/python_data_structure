package shy;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class _107 {
	public List<List<Integer>> levelOrderBottom(TreeNode root) {
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		if (root == null)
			return result;
		Queue<TreeNode> queue = new LinkedList<>();
		queue.add(root);
		while (queue.size() > 0) {
			List<Integer> list = new ArrayList<>();
			int size = queue.size();
			for (int i = 1; i <= size; i++) {
				TreeNode tree_node = queue.poll();
				list.add(tree_node.val);
				if (tree_node.left != null)
					queue.add(tree_node.left);
				if (tree_node.right != null)
					queue.add(tree_node.right);
			}
			result.add(0, list);
		}
		return result;

	}
}
