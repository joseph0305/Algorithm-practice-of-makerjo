/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 #include <set>


void insertAthead(ListNode*& head, int data) 
{ 
    ListNode* n = new ListNode(data); 
    n->next = head; 
    head = n; 
} 

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {

        set<int> s;

        struct ListNode* cursor = new ListNode;
        // node data들을 set에 넣기
        if(head == NULL) {
            cout<<"The head is NULL";
        } else {
            cursor = head;
            while(cursor != NULL) {
                cout<<cursor->val<<" ";
                s.insert(cursor->val);
                cursor = cursor->next;
            }
        }
        
        // === Delate all Nodes ====

        // 이 코드를 함수로 만들어 사용하려 하였으나 왜 인지는 모르겠지만 
        // delete 한 포인터를 참조하게 된다고 오류가 뜸 왜일까요.. 아마 replit 자체에서 head를 이 class 안에서만 사용하게끔 하는 제약 등 같은게 충돌을 초래했을 수도 
         ListNode* temp = new ListNode();

        //head = head->next;
        while(head != NULL) {
            temp = head;
            head = head->next;
            //free(temp);
            delete temp;
        }
        // ==========================

        // set data들을 다시 node에 넣기
        for (set<int>::reverse_iterator rit = s.rbegin(); rit != s.rend(); ++rit) {
            cout << *rit ;
            cout << "test" <<"\n";
		    insertAthead(head,*rit);
	    }
        
    return head;
    }
};


// better solution from somebody else
// 내가 조금 부족한 부분 수정함 ( 메모리 free , continue 부분을 if else 로 수정함


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp=head;
        ListNode* plate;
        while (temp&&temp->next)
        {
            if (temp->next->val==temp->val)
            {
                plate = temp->next;
                temp->next=temp->next->next;
                delete plate;
            }
            else{
                temp=temp->next;    
            }
        }
        return head;
    }
};
