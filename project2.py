class Node:
    nodes = []
    def __init__(self, id='', domain=[], color='', neighbor=[]):
        self.id = id
        self.domain = domain
        self.color = color
        self.neighbor = neighbor

    def add_nodes(self, name, domain=[]):
        node = Node(name, domain)
        self.nodes.append(node)

    def add_neighbor(self, n1, n2):
        neinode = list(self.nodes[n1].neighbor)
        neinode.append(n2)
        self.nodes[n1].neighbor = neinode

    # def add_pass_color(self, p, p_color_list):
    #     p_color = list(self.nodes[p].color)
    #     p_color_list.append(p_color)
    #     return p_color_list

    def find_color(self, p):
        print(self.nodes[p].color)

    def check_nodes_info(self):
        print("")
        for node in self.nodes:
            print(node.id, end=',')
            print(node.domain, end='\n')

    def color_node(self, id):
        self.nodes[id].color = min(self.nodes[id].domain)

    def set_value(self, id):
        emptylist = []
        emptylist.append(self.nodes[id].color)
        self.nodes[id].domain = emptylist

    def remove_neighbor_value(self, id):
        for i in self.nodes[id].neighbor:
            newdomain = list(self.nodes[nds.index(i)].domain)
            if self.nodes[id].color in newdomain:
                newdomain.remove(self.nodes[id].color)
            self.nodes[nds.index(i)].domain = newdomain

    def check_nodes_info_all(self):
        for node in self.nodes:
            print(node.id, end=',')
            print(node.domain, end=',')
            print(node.color, end=',')
            print(node.neighbor, end='\n')

    def check_nodes_id_and_color(self):
        for node in self.nodes:
            print("node:", node.id, "color:", node.color)

class Variable:
    paths = []
    def __init__(self, tail='', head=''):
        self.tail = tail
        self.head = head

    def add_variable(self, xi, xj):
        var = Variable(xi, xj)
        self.paths.append(var)

    def check_variable_info(self):
        for var in self.paths:
            print(var.tail, end=',')
            print(var.head, end='\n')


if __name__ == '__main__':
    with open('C:/Users/Admin/Desktop/project2/test2.txt') as file:
        str = file.readlines()
    n = int(str[0].split("=")[1])
    # print(n)
    p = Variable()
    nd = Node()
    d = [i for i in range(n)]
    # print(d)
    nds = []
    node_number = 0
    for i in range(1, len(str)):
        tail = str[i].split(",")[0].strip()
        head = str[i].split(",")[1].strip()

        if tail not in nds:
            nds.append(tail)
            nd.add_nodes(tail, d)
            node_number += 1
        if head not in nds:
            nds.append(head)
            nd.add_nodes(head, d)
            node_number += 1

        # print(tail, end=',')
        # print(head, end='\n')
        p.add_variable(tail, head)

        t = nds.index(tail)
        h = nds.index(head)
        nd.add_neighbor(t, head)
        nd.add_neighbor(h, tail)

    # p.check_variable_info()
    # nd.check_nodes_info()
    # print(nds)

    min_num = 100
    pick = -1
    pass_id = []
    pass_node = []
    pass_color = []
    color_list = []
    nd.color_node(0)
    nd.set_value(0)
    nd.remove_neighbor_value(0)
    pick = 0
    pass_id.append(0)
    pass_node.append(nds[0])
    pass_color.append(nd.nodes[0].color)

    while len(pass_id) < len(nds):
        for i in range(len(nds)):
            if i in pass_id:
                continue
            current = len(nd.nodes[i].domain)
            if min_num > current:
                min_num = current
                pick = i
        min_num = 100
        pass_id.append(pick)
        pass_node.append(nds[pick])
        # nd.find_color(pick)

        # print(pick)
        # print(pass_id)
        # print(pass_node)

        nd.color_node(pick)
        nd.set_value(pick)
        nd.remove_neighbor_value(pick)


    # nd.check_nodes_info_all()
    nd.check_nodes_id_and_color()


    #ac_3(n, p.paths)

