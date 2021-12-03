import pandas as pd

suffixes = ["_01","_02","_03","_04","_05","_06","_07","_08","_09","_10","_11"]

for suffix in suffixes:
    # read csv data to a dataframe
    df = pd.read_csv('data' + suffix + '.csv')

    # fill blank with 0
    df.fillna(0, inplace=True)

    # declare a global dictionary of from,to set generated from a column
    global nodes
    nodes = {'from':[], 'to':[]}
    # declare a dictionary of from,to set generated from the matrix
    allNodes = {'from':[], 'to':[]}
    # declare a boolean flag for whether generate from,to or not while there is only one node with value 1 in the column
    flag = True

    # Mode1-Single point skipped
    # if there is no more than one node with value 1 in a column, then no (from,to) for the column.
    # Mode2-Single point preserved
    # as long as there exists node(s) with value 1 in a column, then generate (from,to) for the column.
    # if there is only one node with value 1 in the column, then point to itself.
    # eg. row 2, then (from,to) ==> (2,2)

    # TODO let i == len(values) as the ending of the iteration
    def addNode(i, values):
        # the last node
        if i == len(values) - 1:
            if len(nodes['from']) > 0 and flag == False:
                if values[i] == 1:
                    nodes['to'].append(i)
                else:
                    nodes['from'].pop()
            elif flag:
                if len(nodes['from']) > 1:
                    if values[i] == 1:
                        nodes['to'].append(i)
                    else:
                        nodes['from'].pop()
                elif len(nodes['from']) == 1:
                    if values[i] == 1:
                        nodes['to'].append(i)
                    else:
                        # if there is only one node with value 1 in the column, then point to itself
                        nodes['to'].append(nodes['from'][0])
                else:
                    # when the last node is the only node, point to itself
                    if values[i] == 1:
                        nodes['from'].append(i)
                        nodes['to'].append(i)
        # the node with value 0
        elif values[i] == 0:
            addNode(i + 1, values)
        # the first node with value 1
        elif len(nodes['from']) == 0 and values[i] == 1:
            nodes['from'].append(i)
            addNode(i + 1, values)
        # the node with value 1
        elif i < len(values) - 1 and values[i] == 1:
            nodes['to'].append(i)
            nodes['from'].append(i)
            addNode(i + 1, values)

    # loop through columns of df and skip the first 2 columns ('Date','id')
    for column in df.columns[2:]:
        values = df[column].values
        i = 0
        # generate from,to from current column
        addNode(i, values)
        # add the nodes dictionary to allNodes
        allNodes['from'].extend(nodes['from'])
        allNodes['to'].extend(nodes['to'])
        # reset nodes for next column
        nodes = {'from':[], 'to':[]}

    # declare a dataframe using allNodes
    nodesDf = pd.DataFrame(allNodes)
    # DEBUG
    print(suffix)
    print(nodesDf)
    # deduplicate nodesDf
    nodesDf.drop_duplicates(inplace=True)

    # declare a dataframe of String values
    edgeDf = pd.DataFrame({'from':[""], 'to':[""]})
    # loop through values of nodesDf, and map indexes to book ids
    for i in nodesDf.index:
        fromIdx = nodesDf.loc[i, "from"]
        toIdx = nodesDf.loc[i, "to"]
        edgeDf.at[i, "from"] = df.loc[fromIdx].id
        edgeDf.at[i, "to"] = df.loc[toIdx].id

    # output edgeDf to a csv
    edgeDf.to_csv('edge' + suffix + '.csv', index=False)

print("END.")
