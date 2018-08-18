// https://www.geeksforgeeks.org/stack-data-structure-introduction-program/

// usually implemented with array or linked list implementation. 
// Or direcly using STL library: `#include <stack>`.

// following is an example of re-writing stack class, with extra function `max()`, returns the current max element of the stack.
#include <stack>
template <typename T>

class Stack {
  private: 
    stack<T> s;
    stack<pair<T, int>> aux;
  public:
    const T &max(void) const {
      if(!s.empty()) {
        return aux.top().first;
      }
      throw length_error("empty stack");
    }
}