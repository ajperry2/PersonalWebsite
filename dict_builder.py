'''
These functions are used to make a tree structure out of Nodes. These nodes
will eventually be used to make a json object and returned
'''
from itertools import groupby
from operator import itemgetter
import json

#add a node to the tree
def addNode(parentNode,
            module,
            class_name,
            topic,
            descrition,
            image
            ):
    newNode=dict()
    newNode['module'] = module
    newNode['class_name'] = class_name
    newNode['topic'] = topic
    newNode['description'] = descrition
    newNode['image'] = image
    parentNode.append(newNode)

#make the tree
def constructJson(text:str):
    #make the parent node
    parentNode = []
    #get data
    lines = text.split('\n')
    titles = lines[0].split(',')
    data_lol = [line.split(',') for line in lines[1:]]
    for row in data_lol:
        module = row[0]
        class_name = row[1]
        topic = row[2]
        descrition = row[3]
        image = row[4]
        addNode(parentNode,
                module,
                class_name,
                topic,
                descrition,
                image
                )
    #making data wide
    class_list = json.loads(json.dumps(parentNode))
    #sort list to group them together efficiently
    class_list.sort(key=itemgetter("class_name"))
    #group by class name
    wide_list = []
    for key, group in groupby(class_list, lambda item: item["class_name"]):
        description_list = []
        #collect descriptions
        for item in group:
            description_list.append(item['description'])
        newNode = dict()
        newNode['module'] = item['module']
        newNode['class_name'] = key
        newNode['topic'] = item['topic']
        newNode['descriptions'] = description_list
        newNode['image'] = item['image']
        wide_list.append(newNode)
    #repeat, this time collapsing by module
    wide_list.sort(key=itemgetter("module"))
    module_list = []
    for key, group in groupby(wide_list, lambda item: item['module']):
        class_list = []
        #collect descriptions
        for item in group:
            class_list.append(item)
        newNode = dict()
        newNode['module'] = key
        newNode['class_info'] = class_list
        module_list.append(newNode)
    return(module_list)

