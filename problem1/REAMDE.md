# 1. Suggest some of the most important cases to check if a node is correctly removed from the tree.


## Solution

At this test suite we test remove func at tree page. I suggest 2 main test cases to cover it

- Test case 1 
~~~
We merely check del button. It simple atomic action for node deletion
~~~

- Test case 2
~~~
Here we delete node with child elements.
Let's look at UI behavior. If it removes correctly, child elements and them subelements shoudn't displayed
Also, we look at neigbours in tree.
~~~


- Addithional test case
~~~
1. Open page with tree
2. Delete Green Tea group.

Juice Group Should still be a child of beverages
~~~


Look at document with Test Suite
- 
\#testdesign #testdocumentation #testcases