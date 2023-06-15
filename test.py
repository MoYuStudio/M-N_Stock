
def range_fixer(ranges):
    # 整理范围顺序 左小右大
    right_range = []
    for range_id in range(len(ranges)):
        if ranges[range_id][0]>ranges[range_id][1]:
            right_range.append([ranges[range_id][1],ranges[range_id][0]])
        else:
            right_range.append(ranges[range_id])

    # 比较范围
    for range_id in range(len(right_range)):
        try:
            if right_range[range_id][1]>right_range[range_id+1][0]:
                print(right_range[range_id],right_range[range_id+1],'true')
            else:
                print('false')
        except:
            pass
    

range1 = [1.001, 9.002]
range2 = [50.002,2.001]
range3 = [100.001, 300.002]

ranges = [range1, range2, range3]

range_fixer(ranges)
