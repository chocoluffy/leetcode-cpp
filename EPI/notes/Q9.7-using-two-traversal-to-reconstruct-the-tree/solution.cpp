// my solution. iterative method. a better solution is recursively build tree by finding range of left and right sub tree.

b_tree* reconstruction(vector<char> &in_order, vector<char> &pre_order) {
  b_tree* root = create_node(pre_order[0]);
  for (int i = 0; i < pre_order.size() - 1; i++) {
    b_tree* curr = root, prev;
    for (int j = 0 ; j < i; j++) {
      prev = curr;
      bool at_left = true;
      if (if_at_left(pre_order[j], pre_order[i], in_order)) { // j is at left to i, insert to curr->left;
        curr = curr->left;
        at_left = true
      } 
      else { // j is at right to i, insert to curr->right.
        curr = curr->right;
        at_left = false;
      }
    }
    if (at_left) {
     prev->left = curr;
    }
    else {
     prev->right = curr;
    }
  }
}

bool if_at_left(char a, char b, vector<char> seq) {
  bool has_met = false;
  for (int i = 0; i < seq.size(); i++) {
    if (seq[i] == b) {
      has_met = true;
    }
    if (seq[i] == a && !has_met) {
      return true;
    }
    else if (seq[i] == a && has_met) {
      return false;
    }
  }
}