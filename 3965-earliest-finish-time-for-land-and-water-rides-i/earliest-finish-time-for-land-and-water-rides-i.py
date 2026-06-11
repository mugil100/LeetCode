class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l_to_w = float("inf")
        w_to_l = float("inf")
        #land to water
        for i in range(len(landStartTime)):
            land_time = landStartTime[i] + landDuration[i] #6

            for j in range(len(waterStartTime)):
                #if landtime < water start time -> 9-6=3
                if land_time < waterStartTime[j]:
                    water_time = (waterStartTime[j] - land_time) + waterDuration[j]
                #if landtime >= watertime -> 6-9 = 0 

                else:
                    water_time = waterDuration[j]
                
                if land_time + water_time < l_to_w:
                    l_to_w = land_time + water_time

        #water to land
        for i in range(len(waterStartTime)):
            water_time = waterStartTime[i] + waterDuration[i] #6

            for j in range(len(landStartTime)):
                if water_time < landStartTime[j]:
                    land_time = (landStartTime[j] - water_time) + landDuration[j]

                else:
                    land_time = landDuration[j]
                
                if land_time+ water_time < w_to_l:
                    w_to_l = land_time + water_time

        return w_to_l if w_to_l < l_to_w else l_to_w






        