from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # storage dict
        self.store = {}
        self.limit = limit
        # current number of node LRU cache has
        self.node_num = 0
        #DLL to hold key and val pair in correct order 
        self.order_track = DoublyLinkedList()
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #if val at key not in cache, return None
        if key not in self.store:
            return None
        #if present, move to end of DLL and return value
        get_node = self.store[key]
        self.order_track.move_to_end(get_node)
        return get_node.value[1]
        pass

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.store:
            node = self.store[key]
            node.value = (key, value)
            self.order_track.move_to_end(node)
            return
        self.order_track.add_to_tail((key, value))
        self.store[key] = self.order_track.tail
        self.node_num += 1
        if self.node_num > self.limit:
            del self.store[self.order_track.head.value[0]]
            self.order_track.remove_from_head()
            self.node_num -= 1
        pass
