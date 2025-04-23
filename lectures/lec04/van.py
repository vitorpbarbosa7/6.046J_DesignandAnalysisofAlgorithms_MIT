import math

class VEB:
    def __init__(self, universe_size):
        self.u = universe_size
        self.min = None
        self.max = None
        if universe_size <= 2:
            self.summary = None
            self.cluster = []
        else:
            self.cluster_size = int(math.sqrt(self.u))
            self.summary = VEB(self.cluster_size)
            self.cluster = [VEB(self.cluster_size) for _ in range(self.cluster_size)]

    def high(self, x):
        return x // self.cluster_size

    def low(self, x):
        return x % self.cluster_size

    def index(self, i, j):
        return i * self.cluster_size + j

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
            return
        if x < self.min:
            x, self.min = self.min, x
        if self.u > 2:
            h = self.high(x)
            l = self.low(x)
            if self.cluster[h].min is None:
                self.summary.insert(h)
            self.cluster[h].insert(l)
        if x > self.max:
            self.max = x

    def successor(self, x):
        print('Stack frame created\n')
        breakpoint()
        if self.u <= 2:
            if x == 0 and self.max == 1:
                print('Found it, return it')
                breakpoint()
                return 1
            else:
                print('Did not found it')
                breakpoint()
                return None
        elif self.min is not None and x < self.min:
            print('Found, return minimum')
            breakpoint()
            return self.min
        else:
            h = self.high(x)
            i = self.low(x)
            breakpoint()
            max_low = self.cluster[h].max
            if max_low is not None and i < max_low:
                print('Look inside the same cluster')
                breakpoint()
                offset = self.cluster[h].successor(i)
                return self.index(h, offset)
            else:
                print('look in another cluster, summary')
                breakpoint()
                succ_cluster = self.summary.successor(h)
                if succ_cluster is None:
                    return None
                offset = self.cluster[succ_cluster].min
                return self.index(succ_cluster, offset)
            
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.u <= 2:
            return f"VEB(u={self.u}, min={self.min}, max={self.max})"
        summary_str = str(self.summary) if self.summary else "None"
        cluster_bits = [1 if cluster.min is not None else 0 for cluster in self.cluster]
        return (
            f"VEB(u={self.u}, min={self.min}, max={self.max},\n"
            f"     clusters={cluster_bits},\n"
            f"     summary={summary_str})"
        )

# Build VEB tree and insert values from the binary vector
bit_vector = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1]
veb = VEB(len(bit_vector))
for i, bit in enumerate(bit_vector):
    if bit == 1:
        veb.insert(i)


suc = veb.successor(1)
print(suc)
# Let's find successors for values 0 through 15
# successors = {i: veb.successor(i) for i in range(len(bit_vector))}
# successors
