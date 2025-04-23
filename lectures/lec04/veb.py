from math import floor, ceil, log2
from typing import Optional

class VEBTree:
    def __init__(self, u):
        self.u = u
        self.min = None
        self.max = None
        if u <= 2:
            self.summary = None
            self.cluster = None
        else:
            self.lower_sqrt = 2 ** floor(log2(u) / 2)
            self.upper_sqrt = 2 ** ceil(log2(u) / 2)
            self.summary = VEBTree(self.upper_sqrt)
            self.cluster = [VEBTree(self.lower_sqrt) for _ in range(self.upper_sqrt)]

    def __repr__(self):
        return f"VEB(u={self.u}, min={self.min}, max={self.max})"

    def __str__(self):
        if self.u == 2:
            return f"VEB(2): min={self.min}, max={self.max}"
        else:
            return f"VEB({self.u}): min={self.min}, max={self.max}, clusters={len(self.cluster)}"

    def high(self, x):
        return x // self.lower_sqrt

    def low(self, x):
        return x % self.lower_sqrt

    def index(self, x, y):
        return x * self.lower_sqrt + y

    def minimum(self):
        return self.min

    def maximum(self):
        return self.max

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
        else:
            if x < self.min:
                x, self.min = self.min, x
            if self.u > 2:
                h = self.high(x)
                l = self.low(x)
                if self.cluster[h].min is None:
                    self.summary.insert(h)
                    self.cluster[h].insert(l)
                else:
                    self.cluster[h].insert(l)
            if x > self.max:
                self.max = x

    def successor(self, x):
        print('Stack frame created')
        breakpoint()
        if self.u == 2:
            print('Base case 1')
            breakpoint()
            if x == 0 and self.max == 1:
                # Here it can be the fucking magic 
                # where it came from another cluster behind it (0)
                # the next cluster self.max == 1 exists with numbers
                # then we return him 
                return 1
            else:
                return None
        elif self.min is not None and x < self.min:
            print('Base Case 2')
            breakpoint()
            return self.min
        else:
            h = self.high(x)
            l = self.low(x)
            max_low = self.cluster[h].maximum()
            if max_low is not None and l < max_low:
                offset = self.cluster[h].successor(l)
                return self.index(h, offset)
            else:
                succ_cluster = self.summary.successor(h)
                print(f'Next cluster with the sucessor is: {succ_cluster}')
                breakpoint()
                if succ_cluster is None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].minimum()
                    returned_value = self.index(succ_cluster, offset)
                    print(f'Offset returned was {offset}')
                    print(f'Our returned value is {returned_value}')
                    breakpoint()
                    return returned_value
# Adding global recursion depth counter and enhanced debug prints
RECURSION_DEPTH = 0

def veb_debug_print(message):
    indent = "    " * RECURSION_DEPTH
    print(f"{indent}### !!! {message} !!! ###")

# Update the VEBTree.successor method with layered debug output
def enhanced_successor(self, x):
    global RECURSION_DEPTH
    veb_debug_print(f"ENTERING VEB({self.u}) with x = {x}, min = {self.min}, max = {self.max}")
    RECURSION_DEPTH += 1
    print('Stack frame created')
    breakpoint()
    if self.u == 2:
        print('Base case 1')
        breakpoint()
        RECURSION_DEPTH -= 1
        if x == 0 and self.max == 1:
            veb_debug_print("!!! RETURNING 1 FROM BASE CASE (u==2) !!!")
            return 1
        else:
            veb_debug_print("!!! RETURNING NIL FROM BASE CASE (u==2) !!!")
            return None
    elif self.min is not None and x < self.min:
        print('Base Case 2')
        breakpoint()
        RECURSION_DEPTH -= 1
        veb_debug_print(f"!!! RETURNING min = {self.min} BECAUSE x < min !!!")
        return self.min
    else:
        h = self.high(x)
        l = self.low(x)
        max_low = self.cluster[h].maximum()
        if max_low is not None and l < max_low:
            offset = self.cluster[h].successor(l)
            result = self.index(h, offset)
            RECURSION_DEPTH -= 1
            veb_debug_print(f"!!! RETURNING from same cluster[{h}] with offset {offset} → {result} !!!")
            return result
        else:
            succ_cluster = self.summary.successor(h)
            print(f'Next cluster with the successor is: {succ_cluster}')
            breakpoint()
            if succ_cluster is None:
                RECURSION_DEPTH -= 1
                veb_debug_print("!!! RETURNING NIL — no successor cluster found !!!")
                return None
            else:
                offset = self.cluster[succ_cluster].minimum()
                returned_value = self.index(succ_cluster, offset)
                print(f'Offset returned was {offset}')
                print(f'Our returned value is {returned_value}')
                breakpoint()
                RECURSION_DEPTH -= 1
                veb_debug_print(f"!!! RETURNING from different cluster[{succ_cluster}] with offset {offset} → {returned_value} !!!")
                return returned_value

# Inject the enhanced method into the class without removing user's original code
VEBTree.successor = enhanced_successor

# Example usage of the VEBTree with the CLRS Figure 20.6 dataset
def example_usage():
    veb = VEBTree(16)
    dataset = [2, 3, 4, 5, 7, 14, 15]

    for value in dataset:
        veb.insert(value)

    # Debug case: successor(7)
    x = 7
    result = veb.successor(x)
    print(f"Successor of {x} is {result}")

example_usage()
