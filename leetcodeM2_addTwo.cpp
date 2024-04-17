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
void append(int data , ListNode* head) {
        // 새로운 노드 생성
       ListNode* newNode = new ListNode;
        newNode->val = data;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
        } else {
            // 연결리스트가 비어있지 않을 경우
            ListNode* current = head;
            // 마지막 노드 찾기
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = newNode;
        }
    }


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        unsigned long long l1_num = 0; 
        unsigned long long l2_num = 0;

        ListNode* temp = new ListNode;
        unsigned long long j = 1;
        temp = l1;
        while( temp != NULL){
            l1_num += temp->val * j;
            j *= 10;
            temp = temp->next;
        }

        temp = l2;
        j = 1;
        while( temp != NULL){
            l2_num += temp->val * j;
            j *= 10;
            temp = temp->next;
        }
        unsigned long long sum = l1_num + l2_num;
        cout << l1_num << " " << l2_num << '\n';
        cout << sum;
        int result = 0;
        temp = l1;
        while( sum != 0){
            result = sum % 10;
            if(temp != NULL){
                temp->val = result;
                temp = temp->next;
            }
            else{
                append(result,l1);
            }
            sum /= 10;
        }

        return l1;
    }
};


// 첫 번쨰 솔루션
// unsigned long long 을 배정해도 testcase를 통과못함 , 메모리를 넘어가는 숫자 발생




/// 아래 있는 건 다른 사람 솔루션 , 일의자리 수 한자리씩 따로 계산

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
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = new ListNode;
        ListNode* head = temp;
        int total = 0;
        int carry =0;
        while( l1 || l2 || carry){
            total = carry;

            if(l1){
                total += l1->val;
                l1 = l1->next;
            }
            if(l2){
                total += l2->val;
                l2 = l2->next;
            }

            temp->next = new ListNode(total%10);
            carry = total /= 10;
            temp = temp->next;
        }
        return head->next;
    }
};