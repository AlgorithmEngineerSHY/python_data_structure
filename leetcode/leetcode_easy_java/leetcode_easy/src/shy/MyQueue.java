package shy;

import java.util.Stack;

public class MyQueue {
	private Stack<Integer> stack = new Stack<Integer>();
	private Stack<Integer> tmp = new Stack<Integer>();

	public void push(int x) {
		while (!stack.isEmpty())
			tmp.push(stack.pop());
		stack.push(x);
		while (!tmp.isEmpty()) {
			stack.push(tmp.pop());
		}
	}

	public int pop() {
		return stack.pop();
	}

	public int peek() {
		return stack.peek();
	}

	public boolean empty() {
		return stack.isEmpty();
	}
}
