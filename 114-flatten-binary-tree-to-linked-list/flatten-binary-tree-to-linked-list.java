/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        helper(root);
    }

    private TreeNode helper(TreeNode root){
        if(root == null){
        return null;
        }

        TreeNode left_tail = helper(root.left);
        TreeNode right_tail = helper(root.right);

        if (root.left != null){
            left_tail.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        //as we are not sure if we have the left or right or root
        TreeNode last = (right_tail !=null)? right_tail : (left_tail != null ? left_tail : root);


        return last;
        }
}