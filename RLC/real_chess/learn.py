
class TreeSearch(object):

    def __init__(self,agent,env,gamma,lamb):
        self.agent = agent
        self.env = env
        self.gamma = gamma
        self.lamb = lamb

    def search_tree(self,board):
        """
        Search Monte Carlo Style
        Returns:

        """
        #get action values
        #select greedy action and uniform random action



        if board.result()=="*":
            reward = self.gamma * self.lamb * self.search_tree(board)
        elif board.result() == "1-0":
            reward = 1
        elif board.result() == "1/2-1/2":
            reward = 0.5
        elif board.result() == "0-1":
            reward=0
        else:
            print("invalid board")
        return reward






