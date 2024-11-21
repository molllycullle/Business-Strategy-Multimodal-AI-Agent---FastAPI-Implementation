import numpy as np

class FeedbackReinforcementLearning:
    def __init__(self):
        self.weights = np.random.rand(4)

    def update_weights(self, feedback):
        learning_rate = 0.1
        self.weights += learning_rate * np.array(feedback)

if __name__ == "__main__":
    feedback = [1, -1, 1, 0]  # Example feedback
    rl = FeedbackReinforcementLearning()
    print("Initial Weights:", rl.weights)
    rl.update_weights(feedback)
    print("Updated Weights:", rl.weights)
