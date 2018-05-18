// ListNode.h
#ifndef _LISTNODE_H
#define _LISTNODE_H

#include <cstdlib>

typedef int ItemType;

class ListNode {
  friend class LList;
  friend std::ostream& operator<<(std::ostream &os, const LList &list);
  
public:
  ListNode(ItemType item, ListNode* rLink=NULL, ListNode* lLink = NULL);
  
private:
  ItemType item_;
  ListNode *rLink_;
  ListNode *lLink_;
};

inline ListNode::ListNode(ItemType item, ListNode *rLink, ListNode *lLink)
{
  item_ = item;
  rLink_ = rLink;
  lLink_ = lLink;
}

std::ostream& operator<<(std::ostream &os, const LList &list);

#endif // _LISTNODE_H
