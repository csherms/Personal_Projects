def merge_sort(unsorted_list): 
        print("Sorting: ", unsorted_list)
        if len(unsorted_list) == 1: 
            return unsorted_list 

        mid_point = int((len(unsorted_list))/2) 

        first_half = unsorted_list[:mid_point] 
        second_half = unsorted_list[mid_point:] 

        half_a = merge_sort(first_half) 
        half_b = merge_sort(second_half) 
        
        print("Merging: ",unsorted_list)
        return merge(half_a, half_b)



def merge(first_sublist, second_sublist): 
        i = j = 0 
        merged_list = [] 

        while i < len(first_sublist) and j < len(second_sublist): 
            if first_sublist[i] < second_sublist[j]: 
                merged_list.append(first_sublist[i]) 
                i += 1 
            else: 
                merged_list.append(second_sublist[j]) 
                j += 1 

        while i < len(first_sublist): 
            merged_list.append(first_sublist[i]) 
            i += 1 

        while j < len(second_sublist): 
            merged_list.append(second_sublist[j]) 
            j += 1 

        return merged_list
        

   
myList = [55,  31,  26,  20,  63,  7,  51,  74,  81,  40] 

print("Sorted List: " + str(merge_sort(myList)))
