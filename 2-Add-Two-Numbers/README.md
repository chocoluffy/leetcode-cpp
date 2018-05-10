# 思路(C++)

重点在implementation。

想清楚什么时候需要引入dummy node。常见的原因是为了更简便地处理while loop里面的edge case，比如这里的第一个node的初始化。我们创建新node是依赖while loop的逻辑的，如果为NULL，在loop使用node->next会seg fault。所以通过创建dummy node使得可以直接在loop里使用node->next。然后最后用dummy->next返回整个链的head。