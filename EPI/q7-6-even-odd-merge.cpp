// Q: given a list <l0, l1, l2, ...>, modify it into <l0, l2, l4,..., l1, l3...> a even-odd merged list.
// 多指针同时遍历的技巧。prev的使用。以及corner case针对even\odd的讨论。一个技巧是，根据已有的变量是否会seg fault来判断需要新增的case，最常见的遗漏就是对是否为null的讨论（针对linked list是否为空等等）。
node* even_odd_merge(node* L) {
  node* prev_even = NULL;
  node* even = L, odd = L.next;
  node* odd_start = L.next;
  while(even && odd) {
    prev_even = even;
    even.next = odd.next;
    even = even.next;
    if(even) {
      odd.next = even.next;
      odd = odd.next;
    }
  }  	
  if(even) { // case: odd number of elements in list.
    prev_even = even;
  }
  if(prev_even) { // case: empty list.
    prev_even.next = odd_start;
  }
  return L;
}	