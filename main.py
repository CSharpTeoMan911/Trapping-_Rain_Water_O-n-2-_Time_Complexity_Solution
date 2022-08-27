
# Time complexity:
#
# Best: O(n / 2)
#
# Worst: O(n / 2)
#
# Average: O(n / 2)





def Trapping_The_Water(reservoir_dimensions):

    value_changed_left = False

    value_changed_right = False

    previous_lowest_limit_value = 0

    cumulated_water = 0

    lowest_limit_value = 0

    container_limit_left = reservoir_dimensions[0]

    container_limit_right = reservoir_dimensions[len(reservoir_dimensions) - 1]




    for index in range(1, len(reservoir_dimensions) - 1, 1):


        reverse_index = len(reservoir_dimensions) - 1 - index


        if reverse_index > index:

            if container_limit_left < reservoir_dimensions[index]:


                if container_limit_right >= container_limit_left:
                    previous_lowest_limit_value = container_limit_left



                elif container_limit_right <= container_limit_left:
                    previous_lowest_limit_value = container_limit_right


                value_changed_left = True
                container_limit_left = reservoir_dimensions[index]




            if container_limit_right < reservoir_dimensions[reverse_index]:


                if container_limit_right >= container_limit_left:
                    previous_lowest_limit_value = container_limit_left


                elif container_limit_right <= container_limit_left:
                    previous_lowest_limit_value = container_limit_right



                value_changed_right = True
                container_limit_right = reservoir_dimensions[reverse_index]




            if container_limit_right >= container_limit_left:
                lowest_limit_value = container_limit_left


            elif container_limit_right <= container_limit_left:
                lowest_limit_value = container_limit_right

            cumulated_water += (lowest_limit_value - reservoir_dimensions[index]) + (lowest_limit_value - reservoir_dimensions[reverse_index])



            if value_changed_left is True:
                cumulated_water += lowest_limit_value - previous_lowest_limit_value * (len(reservoir_dimensions) - reverse_index)

            elif value_changed_right is True:
                cumulated_water += (lowest_limit_value - previous_lowest_limit_value) * (index - 1)









            value_changed_left = False

            value_changed_right = False


    print("Cumulated Water: " + str(cumulated_water))











if __name__ == '__main__':
    reservoir_dimensions = [7, 0, 4, 2, 5, 0, 6, 4, 0, 4]

    Trapping_The_Water(reservoir_dimensions)