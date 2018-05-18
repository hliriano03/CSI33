// LList.cpp
#include "LList2.h"
#include <iostream>

LList::LList() // constructor definition
{
  head_ = NULL; // initially there is no head node
  size_ = 0;    // initially the size of the linked list is 0
}

ListNode* LList::_find(size_t position) // find by index operation
{ // finds the node by index and returns pointer to it
  ListNode *node = head_; // initially node points to the head
  size_t i;

  for (i=0; i<position; i++) {
    node = node->lLink_; // jumping from one node to the other, same as (*node).link_
  }
  return node; // return the pointer, not the 'value' to which is points
}

ItemType LList::_delete(size_t position) // delete by index operation
{ // returns the value of the node being deleted
  ListNode *node, *dnode; 
  ItemType item;

  if (position == 0) { // in case if we are deleating the head node
    dnode = head_;
    head_ = head_->lLink_;
    item = dnode->item_;
    delete dnode;
  }
  else {
    node = _find(position - 1); // find the node at the previous position
    if (node != NULL) {
      dnode = node->lLink_;
      node->lLink_ = dnode->lLink_;
      item = dnode->item_;
      delete dnode;
    }
  }
  size_ -= 1; // decrease the size of the linked list
  return item;
}                

void LList::append(ItemType x) // append operation
{ // appends to the end of the list
  ListNode *node, *newNode = new ListNode(x);
  
  if (head_ != NULL) { // if the linked list not empty
    node = _find(size_ - 1);
    node->lLink_ = newNode;
  }
  else {
    head_ = newNode;
  }
  size_ += 1; // increment the size of the linked list
}

void LList::insert(size_t i, ItemType x) // insert into position i
{
  ListNode *node;
  
  if (i == 0) { // inserting into the head position
    head_ = new ListNode(x, head_);
  }
  else {
  	node = _find(i - 1); // find the node at the previous position
    node->lLink_ = new ListNode(x, node->lLink_);
  }
  size_ += 1; // increment the size of the linked list
}

ItemType LList::pop(int i) // pop operation
{
  if (i == -1) { // myLList.pop(-1) will mean "delete the last element"
    i = size_ - 1;
  }
  return _delete(i); // call the helper method, 
  // which deletes element at position i and returns the value
}

ItemType& LList::operator[](size_t position) // myLList[i] operator
{ // returns reference to the value of the node, 
  // which allows to not only access, but to change the value
  ListNode *node;

  node = _find(position);
  return node->item_;
}

LList::LList(const LList& source) // copy constructor
{
  copy(source); // calling helper method
}

void LList::copy(const LList &source) // helper method for copy constructor
{
  ListNode *snode, *node; // snode is the source list's info

  snode = source.head_;
  node = head_ = snode;
  if (snode) { // same as  snode != NULL
    node = head_ = new ListNode(snode->item_);
    snode = snode->lLink_; // proceeding to the next node in the source list
  }
  while (snode) {
    node->lLink_ = new ListNode(snode->item_);
    node = node->lLink_;
    snode = snode->lLink_;
  }
  size_ = source.size_; // recording the size
}

LList& LList::operator=(const LList& source) //assignment operator
{
  dealloc(); // first, delete all information about current list
  copy(source); // copy all the information from source list
  return *this;
}

LList::~LList() // destructor
{
  dealloc(); // calling the helper method
}

void LList::dealloc() // helper method
{ // deallocates all nodes in the list
  ListNode *node, *dnode;

  node = head_;
  while (node) {
    dnode = node;
    node = node->lLink_;
    delete dnode;
  }
}

std::ostream& operator<<(std::ostream &os, const LList &list) {
	ListNode *node;
	
	node = list.head_;
	
	while (node->lLink_) {
		os << node->item_ << ", ";
		node = node->lLink_;
	}
	os << node->item_;

	return os;
}
