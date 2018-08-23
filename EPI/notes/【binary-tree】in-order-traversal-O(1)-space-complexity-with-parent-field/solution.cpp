// a bst, each node has a parent field. show a in-order traversal of that bst. space complexity O(1). only require one prev pointer.
void in_order_traversal(node* root) {
  node* curr = root, prev;
  while(curr) {
    if (!curr) { // if reach nullptr;
      prev = curr;
      curr = curr->parent;
    }
    else {
      if (curr->left && prev != curr->left) {
        prev = curr;
        curr = curr->left;
      } 
      else if (!curr->left) { // reach leave, go to parent.
        prev = curr;
        cout << curr << endl;
        curr = curr->parent;
      }
      else { // left subtree visited, go to curr->right;
        prev = curr;
        cout << curr << endl;
        curr = curr->right;
      }
    }
  }
}