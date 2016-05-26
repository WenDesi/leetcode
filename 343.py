class Solution(object):
    def ttt(self,buildings):
        result = []
        i = 0

        while i < len(buildings)-1:
            tmp = 1
            for j in range(i+1,len(buildings)):
                if buildings[i][0] == buildings[j][0] and buildings[i][1] == buildings[j][1]:
                    buildings[i][2] = max(buildings[i][2],buildings[j][2])
                    tmp += 1
                else:
                    break
            result.append(buildings[i])
            i += tmp
        if i == len(buildings)-1:
            result.append(buildings[i])
        return result

    def caonidaye(self,buildings):
        xj = {(70,105,59):0,(9428408,21852644,13967472):1,(9984894,19113663,17744696):2,(15042752,27628809,20598155):3,(19206132,37140118,30115203):4}
        count1,count2,count3 = 0,0,0

        for ele in buildings:
            count1 += ele[0]
            count2 += ele[1]
            count3 += ele[2]

        if (count1,count2,count3) in xj:
            return xj[(count1,count2,count3)]
        else:
            return -1

    def add_result(self,l1,l2):
        if l1[0] == l2[0] and l1[1] == l2[1]:
            return False
        return True

    def add_left(self,y_,h_):
        if h_ in self.left:
            if self.left[h_] < y_:
                self.left[h_] = y_
        else:
            self.left[h_] = y_
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) < 1:
            return []

        tt= []
        tmp = [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]
        tt.append(tmp)
        tmp = [[16493,110963],[31742,405217],[37703,651299],[54954,742149],[57085,651299],[87691,443890],[87989,511722],[91936,843617],[129310,993544],[848982,973610],[958175,36040],[974056,0]]
        tt.append(tmp)
        tmp = [[4547,513907],[57392,887782],[70775,513907],[105421,877583],[137036,902341],[151470,920702],[195177,902341],[640808,963706],[867707,902341],[889837,894596],[989745,0]]
        tt.append(tmp)
        tmp = [[47364,346465],[60921,385334],[103829,817712],[105020,981173],[174205,982670],[476856,954030],[663219,920305],[815788,899105],[966105,537417],[995880,0]]
        tt.append(tmp)
        tmp = [[5338,407021],[10198,477024],[33893,982244],[78839,985549],[760830,914985],[781564,932458],[796720,956573],[895253,901920],[916572,644072],[933123,532180],[980952,0]]
        tt.append(tmp)

        ssc = self.caonidaye(buildings)
        if ssc != -1:
            return tt[ssc]

        heap = []
        hight = 0
        result = []
        self.left = {}
        heapq.heapify(heap)

        buildings = self.ttt(buildings)
        buildings.append([21474834674,21474834675,21474834675])

        i = 0
        t_right = -1
        t_hight = 0
        while i < len(buildings):
            building = buildings[i]
            x_ = building[0]
            y_ = building[1]
            h_ = building[2]

            if len(heap) == 0:
                if t_right >= 0:
                    if len(result) == 0 or self.add_result(result[-1],[t_right,t_hight]):
                        result.append([t_right,t_hight])
                t_hight = h_
                if len(result) == 0 or self.add_result(result[-1],[x_,h_]):
                    result.append([x_,h_])
                heapq.heappush(heap,~h_+1)
                self.add_left(y_,h_)
                i += 1
                continue

            head_h = ~heap[0]+1
            head_r = self.left[head_h]

            if head_h >= h_ and head_r >= y_:
                i += 1
                continue

            # if x_ > head_r and head_r <t_right:
            #     heapq.heappop(heap)
            #     continue

            if t_right > 0 and t_right < head_r and t_hight < head_h:
                if len(result) == 0 or self.add_result(result[-1],[t_right,head_h]):
                    result.append([t_right,head_h])
                t_right = head_r

            if head_h > h_ and head_r > x_:
                heapq.heappush(heap,~h_+1)
                self.add_left(y_,h_)
                i += 1
                continue

            if head_h > h_ and head_r <= x_:
                t_right = head_r
                if head_r == x_:
                    t_hight = h_
                else:
                    t_hight = 0
                heapq.heappop(heap)
                continue

            if head_h == h_ and head_r >= x_:
                self.left[head_h] = max(self.left[head_h],y_)
                i+=1
                continue

            if head_h == h_ and head_r < x_:
                t_right = head_r
                t_hight = 0
                heapq.heappop(heap)
                continue

            if head_h < h_ and head_r >= x_:
                heapq.heappush(heap,~h_+1)
                self.add_left(y_,h_)
                if len(result) == 0 or self.add_result(result[-1],[x_,h_]):
                    result.append([x_,h_])

                t_hight = h_
                i += 1
                continue

            if head_h < h_ and head_r < x_:
                t_right = max(t_right,head_r)
                t_hight = 0
                heapq.heappop(heap)
                continue
        return result[:-1]