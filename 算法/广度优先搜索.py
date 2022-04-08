"""
广度优先搜索指出是否有从A到B的路径。
 如果有，广度优先搜索将找出最短路径。
有向图中的边为箭头，箭头的方向指定了关系的方向，例如，rama→adit表示rama欠adit钱。
 无向图中的边不带箭头，其中的关系是双向的，例如，ross - rachel表示“ross与rachel约
会，而rachel也与ross约会”
队列是先进先出（FIFO）的。  类似于排队上公交 先排先进 后来到后面排队
 栈是后进先出（LIFO）的。  函数里调用函数 就是调用栈 后进先出
你需要按加入顺序检查搜索列表中的人，否则找到的就不是最短路径，因此搜索列表必
须是队列。
 对于检查过的人，务必不要再去检查，否则可能导致无限循环
"""

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#判断是否是名字以m结尾函数
def person_is_seller(name):
    return name[-1] == 'm'

#主函数
def search(name):
    """
    A=deque([]) #创建一个空的双队列
    A.append(n) #从右边像队列中增加元素 ，n表示增加的元素
    A.appendleft(n) #从左边像队列中增加元素，n表示增加的元素
    A.clear() #清空队列
    A.count(n) #在队列中统计元素的个数，n表示统计的元素
    A.extend(n) #从右边扩展队列，n表示扩展的队列
    A.extendleft(n) #从左边扩展队列，n表示扩展的队列
    A.pop() #从队列的右边删除元素，并且返回删除值
    A.popleft() #从队列的左边删除元素，并且返回删除值
    A.remove(n) #从队列中删除指定的值‘
    A.reverse() #翻转队列
    A.rotate(n) #旋转队列，默认时值为1，由右边开始旋转，负值代表左边旋转，n代表从队列的第一个元素开始，n从1开始计数
    ————————————————
    版权声明：本文为CSDN博主「旅立の涯秸」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/jamfiy/article/details/88188595

    """
    # deque 创建一个双端队列
    search_queue = deque()
    #将第一个散列表(字典) 键值传入队列
    search_queue += graph[name]
    #创建一个空列表 用于接收校验过的人名
    searched = []
    #循环 只要队列中的值不为空
    while search_queue:
        #popleft：从左边删除第一个值 并返回删除值
        person = search_queue.popleft()
        #判断 person 是否在已校验人列表中存在
        #若在已校验列表中存在 则不进入判断 避免进入死循环
        if person not in searched:
            #判断person是否满足查找条件 调用确定函数
            if person_is_seller(person):
                print(f"{person}这就是你要找的芒果商")
                # print("%s 他就是你要找的经销商" %person)
                #查找到目标 结束循环
                return True
            #当不满足查找条件时
            else:
                #将被查找字典中的person对应的值传入队列后端
                search_queue += graph[person]
                #将以查找过的person人名加入已检验人列表中
                searched.append(person)
    #全部查找完后 无目标 结束循环
    return False
#调用主函数
search("you")