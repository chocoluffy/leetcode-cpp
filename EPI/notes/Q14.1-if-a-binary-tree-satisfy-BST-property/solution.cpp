bool if_bst(tree* curr) {
  if(!curr) return true;
  // find the rightmost node from the left sub tree;
  tree* left_max= curr->left;
  while(left_max) left_max = left_max->right; // (!left_max || curr->val > left_max->val);
  tree* right_min = curr->right;
  while(right_min) right_min = right_min->left;
  return (!left_max || curr->val > left_max->val) && (!right_min || curr->val < right_min->val) && if_bst(curr->left) && if_bst(curr->right);
}