

def mcp_neuron(x1, x2):
    w1 = 1
    w2 = 1
    threshold = 2

    summation = x1*w1 + x2*w2

    if summation >= threshold:
        return 1
    else:
        return 0


inputs = [(0,0), (0,1), (1,0), (1,1)]

print("MCP Neuron AND Gate Output:")
for x1, x2 in inputs:
    print(x1, x2, "->", mcp_neuron(x1, x2))
