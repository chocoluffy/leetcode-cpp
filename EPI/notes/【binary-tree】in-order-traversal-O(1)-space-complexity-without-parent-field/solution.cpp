// a O(1) space complexity method for traversing binary tree, but may need modify the tree, thus not thread safe.
void in_order_traversal(node* root) {
  node* curr = root, last;
  while(curr) {
    if (!curr->left) {
      cout << curr->val << endl; // print current node;
      last = curr;
      curr = curr->right;
    } 
    else { 
      // find curr node's precessor.
      node* pre = curr->left; 
      while(pre && pre->val != curr) {
        pre = pre->right;
      }
      if (pre) { // prev->val == curr, revert the structure back to original.
        pre->right = nullptr;
        cout << curr->val << endl;
        last = curr;
        curr = cur->right;
      } else { // reach precessor, create link.
        prev->right = curr;
        last = curr;
        curr = curr->left;
      } 
    }
  }
}