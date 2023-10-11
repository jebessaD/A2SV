class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #
        curr_dir = 'N'
        curr_pos = [0,0]
        directions = {'N':(0,1), 'E':(1,0), 'W':(-1,0), 'S':(0,-1)}
        change_dir = {
            'N':{'L':'W', 'R':'E'},
            'E':{'L':'N', 'R':'S'},
            'W':{'L':'S', 'R':'N'},
            'S':{'L':'E', 'R':'W'}
        }
        for inst in instructions:
            if inst == 'G':
                curr_pos[1] += directions[curr_dir][1]
                curr_pos[0] += directions[curr_dir][0]
            else:
                curr_dir=change_dir[curr_dir][inst]

        return curr_dir != 'N' or curr_pos == [0,0]
            