Time Complexity is O(n)

import java.util.*;

public class histogram {
    public static void main(String[] args) {
        int[] heights = {8,7,6,5,4,3,2,1};
        Stack<Integer> st = new Stack<>();
        int maxArea = 0;

        for (int i = 0; i < heights.length; i++) {
            while (!st.isEmpty() && heights[i] < heights[st.peek()]) {
                int height = heights[st.pop()];
                int width = st.isEmpty() ? i : (i - st.peek() - 1);
                maxArea = Math.max(maxArea, height * width);
            }
            st.push(i);
        }

        // Final cleanup for remaining stack
        while (!st.isEmpty()) {
            int height = heights[st.pop()];
            int width = st.isEmpty() ? heights.length : (heights.length - st.peek() - 1);
            maxArea = Math.max(maxArea, height * width);
        }

        System.out.println(maxArea);
    }
}
