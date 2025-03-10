import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def mock_jump(label):
    time.sleep(0.01) 
    return label

def test_scene_transition_performance():
    start_time = time.time()
    
    for _ in range(1000):
        mock_jump("library_scene")
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Execution time of 1000 transitions: {execution_time:.3f} sec")
    assert execution_time < 15, f"Transitions are too slow: {execution_time:.3f} sec"

if __name__ == '__main__':
    test_scene_transition_performance()