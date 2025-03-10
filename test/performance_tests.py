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
    
    print(f"Час виконання 1000 переходів: {execution_time:.3f} секунд")
    assert execution_time < 15, f"Переходи занадто повільні: {execution_time:.3f} сек"

if __name__ == '__main__':
    test_scene_transition_performance()