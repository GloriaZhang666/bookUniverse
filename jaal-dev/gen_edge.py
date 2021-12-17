import os
import pandas as pd

# declare a boolean flag for whether generate from,to or not while there is only one node with value 1 in the column
global flag
flag = True

# Mode1-Single point skipped
# if there is no more than one node with value 1 in a column, then no (from,to) for the column.
# Mode2-Single point preserved
# as long as there exists node(s) with value 1 in a column, then generate (from,to) for the column.
# if there is only one node with value 1 in the column, then point to itself.
# eg. row 2, then (from,to) ==> (2,2)
def addNode(i, values):
    # when values loop is over
    if i == len(values):
        # Mode2
        if flag:
            if len(nodes['from']) > 1:
                nodes['from'].pop()
            elif len(nodes['from']) == 1 :
                # if there is only one node with value 1 in the column, then point to itself
                nodes['to'].append(nodes['from'][0])
        else:
            # Mode1
            if len(nodes['from']) > 0:nodes['from'].pop()
    # the node with value 0
    elif values[i] == 0:
        addNode(i + 1, values)
    # the first node with value 1
    elif len(nodes['from']) == 0:
        nodes['from'].append(i)
        addNode(i + 1, values)
    # the node with value 1 besides the first node
    elif i < len(values):
        nodes['to'].append(i)
        nodes['from'].append(i)
        addNode(i + 1, values)

# columns: list of selected columns to generate a view of df
def gen_edge_csv(columns):
    if len(columns) == 0:
        return

    # resolve path
    this_dir, _ = os.path.split(__file__)
    outputName = os.path.join(this_dir, "got", "got_edge_df.csv")
    # read csv data to a dataframe
    df = pd.read_csv(os.path.join(this_dir, "got", "data.csv"))

    # fill blank with 0
    df.fillna(0, inplace=True)

    # number of non-attribute columns
    nonAttributeNo = 3

    # declare a dictionary of from,to set generated from the matrix
    allNodes = {'from':[], 'to':[]}

    # declare a global dictionary of from,to set generated from a column
    global nodes
    nodes = {'from':[], 'to':[]}

    # True: part of attributes combined together to generate graph
    partFlag = True
    if 'All' in columns:
        partFlag = False
        # get all columns of df except for non-attribute columns ('Date','Status','id')
        columns = df.columns[nonAttributeNo:]
    else:
        # reset books df comply with conditions (AND)
        query = ''
        for column in columns:
            query += '`' + column + '` == 1 & '
        df.query(query[:-2], inplace=True)

    # loop through selected columns of df, and generate (from,to) pairs
    for column in df[columns]:
        values = df[column].values
        indexes = df[column].indexes
        print(indexes)
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
    # deduplicate nodesDf
    nodesDf.drop_duplicates(inplace=True)
    print(nodesDf)

    # declare a dataframe of String values
    edgeDf = pd.DataFrame({'from':[""], 'to':[""]})
    # loop through values of nodesDf, and map indexes to book ids
    for i in nodesDf.index:
        fromIdx = nodesDf.loc[i, "from"]
        toIdx = nodesDf.loc[i, "to"]
        edgeDf.at[i, "from"] = df.loc[fromIdx].id
        edgeDf.at[i, "to"] = df.loc[toIdx].id

    # output edgeDf to a csv
    edgeDf.to_csv(outputName, index=False)

    print("gen_edge_csv END.")
