// given a sorted array, build a BST from array of minimum possible height.
node* build_helper(vector<int> array, int start, int end) {
  if (start >= end) {
    node* leave = new Node(array[end], nullptr, nullptr);
    return leave;
  }
  int middle = start + (end - start) / 2;
  node* left_sub = build_helper(array, start, middle);
  node* right_sub = build_helper(array, middle+1, end);
  node* curr = new Node(array[middle], left_sub, right_sub);
  return curr;
}

node* build(vector<int> array) {
	return build_helper(array, 0, array.size());
}

 build({1, 3, 4, 7, 8});