package linkedlist

class ListNode(val `val`: Int, var next: ListNode? = null)

fun partition(head: ListNode?, x: Int): ListNode? {
    var lessThan: ListNode? = null
    var lessThanHead: ListNode? = null
    var greaterThanEqual: ListNode? = null
    var greaterThanHead: ListNode? = null

    var current = head
    while (current != null) {
        if (current.`val` < x) {
            if (lessThanHead != null && lessThan != null) {
                lessThan.next = current
                lessThan = lessThan.next
            } else {
                lessThanHead = current
                lessThan = current
            }

        } else {
            if (greaterThanHead != null && greaterThanEqual != null) {
                greaterThanEqual.next = current
                greaterThanEqual = greaterThanEqual.next
            } else {
                greaterThanHead = current
                greaterThanEqual = current

            }

        }
        current = current.next

    }
    if (lessThan != null) {
        lessThan.next = greaterThanHead
    }
    if (greaterThanEqual != null) {
        greaterThanEqual.next = null
    }

    return if (lessThanHead == null) greaterThanHead else lessThanHead


}
