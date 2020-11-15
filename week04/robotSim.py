class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0
        direx = [0, 1, 0, -1] # 代表x轴的[北，东，南，西]四个方向
        direy = [1, 0, -1, 0] # 代表y轴的[北，东，南，西]四个方向
        curx, cury, curdire, ans = 0, 0, 0, 0 # curdire 当前方向数组下标
        com_len, obs_len = len(commands), len(obstacles)
        obstacles_set = {(obstacles[i][0], obstacles[i][1]) for i in range(obs_len)} # 障碍点的坐标集，x=[i][0],y=[i][1]

        for i in range(com_len):
            if commands[i] == -1: # 右转90度
                curdire = (curdire + 1) % 4 # +1，右转90度
            elif commands[i] == -2: # 左转90度
                curdire = (curdire + 3) % 4 # +3，右转270度 = 左转90度
            else: # 1 < x < 9 向前移动x个单位
                for j in range(commands[i]):
                    nx = curx + direx[curdire] # 尝试走出下一步
                    ny = cury + direy[curdire]
                    if (nx, ny) not in obstacles_set: # 看是否会遇到障碍物
                        curx = nx
                        cury = ny
                        ans = max(ans, curx*curx + cury*cury) # 计算最大距离平方
                    else: # 遇到障碍点， 停住，不能前进，退出当前指令
                        break
        return ans
