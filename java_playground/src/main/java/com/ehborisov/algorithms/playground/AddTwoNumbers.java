package com.ehborisov.algorithms.playground;

/**
 * https://leetcode.com/problems/add-two-numbers/
 */

class AddTwoNumbers {
    public static class ListNode {
          int val;
          ListNode next;
          ListNode() {}
          ListNode(int val) { this.val = val; }
          ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode resultHead = new ListNode();
        int carry = 0;
        ListNode currentPtr = resultHead;
        while(currentPtr != null) {
            currentPtr.val += carry;
            if(l1 != null){
                currentPtr.val += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                currentPtr.val += l2.val;
                l2 = l2.next;
            }
            carry = currentPtr.val / 10;
            currentPtr.val = currentPtr.val % 10;
            if(l1 != null || l2 != null){
                currentPtr.next = new ListNode();
                currentPtr = currentPtr.next;
            } else {
                if(carry != 0) {
                    currentPtr.next = new ListNode(carry);
                }
                currentPtr = null;
            }
        }
        return resultHead;
    }
}