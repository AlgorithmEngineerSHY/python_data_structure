package shy;

import java.util.ArrayList;
import java.util.List;

public class _257 {
	public List<String> binaryTreePaths(TreeNode node) {
		List<String> list = new ArrayList<String>();
		if (node == null)
			return list;
		cuishuo(node, "", list);
		return list;
	}

	public void cuishuo(TreeNode node, String path, List<String> list) {
		if (node.left == null && node.right == null)
			list.add(path + node.val);
		if (node.left != null)
			cuishuo(node.left, path + node.val + "->", list);
		if (node.right != null)
			cuishuo(node.right, path + node.val + "->", list);

	}
}
