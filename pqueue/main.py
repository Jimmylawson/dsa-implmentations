from priority_queue import PriorityQueue




def main():
    pq = PriorityQueue([18,10,1,20,-1,0])
    pq.build_heap()
    print(pq)
    # pq.insert(1)
    # print(pq.peek())
    # print(pq.pop())
    # print(pq)
    # print(pq.isEmpty())
    # pq.insert(-1)
    # print(pq)


if __name__ == "__main__":
    main()